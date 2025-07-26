"""
Mineral Sınıflandırma Web Arayüzü - Gradio ile
"""
import gradio as gr
import numpy as np
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from model_loader import get_classifier

# Global değişkenler
classifier = None

def initialize_model():
    """Modeli başlat"""
    global classifier
    try:
        classifier = get_classifier("./model")
        success = classifier.load_model()
        if success:
            return "✅ Model başarıyla yüklendi!", True
        else:
            return "❌ Model yükleme başarısız!", False
    except Exception as e:
        return f"❌ Hata: {str(e)}", False

def classify_image(image):
    """Görüntüyü sınıflandır"""
    global classifier
    
    if classifier is None or not classifier.is_loaded:
        return "❌ Model henüz yüklenmedi!", None, None
    
    if image is None:
        return "⚠️ Lütfen bir görüntü yükleyin!", None, None
    
    try:
        # Görüntüyü PIL formatına dönüştür
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image).convert("RGB")
        elif not isinstance(image, Image.Image):
            image = Image.open(image).convert("RGB")
        
        # Tahmin yap
        predicted_label, confidence, all_scores = classifier.predict(image)
        
        # Sonuçları formatla
        result_text = f"""
        🎯 **Tahmin Sonucu:** {predicted_label.upper()}
        📊 **Güven Skoru:** {confidence:.2%}
        """
        
        # Tüm skorları sırala
        sorted_scores = sorted(all_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Detaylı sonuçlar
        detailed_results = "📈 **Tüm Sınıf Skorları:**\n\n"
        for i, (mineral, score) in enumerate(sorted_scores):
            emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "📋"
            detailed_results += f"{emoji} **{mineral.capitalize()}:** {score:.2%}\n"
        
        # Grafik için veri hazırla
        minerals = [item[0].capitalize() for item in sorted_scores]
        scores = [item[1] * 100 for item in sorted_scores]  # Yüzdeye dönüştür
        
        # Plotly grafik oluştur
        fig = go.Figure()
        
        # Bar chart ekle
        colors = px.colors.qualitative.Set3[:len(minerals)]
        fig.add_trace(go.Bar(
            x=minerals,
            y=scores,
            name='Güven Skorları',
            marker_color=colors,
            text=[f'{score:.1f}%' for score in scores],
            textposition='auto',
        ))
        
        fig.update_layout(
            title={
                'text': f'🔬 Mineral Sınıflandırma Sonuçları<br><sub>En İyi Tahmin: {predicted_label.upper()} ({confidence:.1%})</sub>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 16}
            },
            xaxis_title='Mineral Türleri',
            yaxis_title='Güven Skoru (%)',
            yaxis_range=[0, 100],
            template='plotly_white',
            showlegend=False,
            height=500,
            margin=dict(t=80, b=50, l=50, r=50)
        )
        
        fig.update_xaxes(tickangle=45)
        
        return result_text, detailed_results, fig
        
    except Exception as e:
        error_msg = f"❌ Sınıflandırma hatası: {str(e)}"
        return error_msg, None, None

def create_interface():
    """Gradio arayüzünü oluştur"""
    
    # CSS stil
    css = """
    .mineral-header {
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .mineral-info {
        background: #27272a;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #007bff;
        margin: 10px 0;
    }
    """
    
    with gr.Blocks(css=css, title="🔬 Mineral Sınıflandırıcı") as demo:
        # Başlık
        gr.Markdown("""
        <div class="mineral-header">
            <h1>🔬 Mineral Sınıflandırma Sistemi</h1>
            <p>Vision Transformer (ViT) modelini kullanarak mineral görüntülerini sınıflandırın</p>
        </div>
        """)
        
        # Model durumu
        with gr.Row():
            model_status = gr.Textbox(
                label="🤖 Model Durumu",
                value="Model yükleniyor...",
                interactive=False
            )
            init_btn = gr.Button("🔄 Modeli Yeniden Yükle", variant="secondary")
        
        gr.Markdown("""
        <div class="mineral-info">
            <h3>📋 Desteklenen Mineral Türleri:</h3>
            <ul>
                <li><strong>Biotite:</strong> Koyu renkli mika minerali</li>
                <li><strong>Bornite:</strong> Bakır sülfür minerali</li>
                <li><strong>Chrysocolla:</strong> Bakır silikat minerali</li>
                <li><strong>Malachite:</strong> Yeşil bakır karbonat minerali</li>
                <li><strong>Muscovite:</strong> Açık renkli mika minerali</li>
                <li><strong>Pyrite:</strong> Altın renginde demir sülfür minerali</li>
                <li><strong>Quartz:</strong> Kristal silisyum oksit minerali</li>
            </ul>
        </div>
        """)
        
        # Ana arayüz
        with gr.Row():
            with gr.Column(scale=1):
                # Görüntü yükleme
                image_input = gr.Image(
                    label="📷 Mineral Görüntüsü Yükleyin",
                    type="pil",
                    height=400
                )
                
                classify_btn = gr.Button(
                    "🔍 Görüntüyü Sınıflandır", 
                    variant="primary",
                    size="lg"
                )
                
                # Örnek görüntü butonları
                gr.Markdown("### 📌 İpuçları:")
                gr.Markdown("""
                - Görüntü kaliteli ve net olmalı
                - Mineral tek başına ve iyi aydınlatılmış olmalı
                - JPEG, PNG formatları desteklenmektedir
                - Optimal boyut: 224x224 piksel veya daha büyük
                """)
            
            with gr.Column(scale=1):
                # Sonuçlar
                result_output = gr.Markdown(
                    label="🎯 Sınıflandırma Sonucu",
                    value="Henüz görüntü yüklenmedi..."
                )
                
                detailed_output = gr.Markdown(
                    label="📊 Detaylı Sonuçlar",
                    visible=False
                )
                
                # Grafik
                plot_output = gr.Plot(
                    label="📈 Güven Skorları Grafiği",
                    visible=False
                )
        
        # Event handlers
        def on_classify(image):
            result, detailed, plot = classify_image(image)
            return (
                result,
                gr.update(value=detailed, visible=detailed is not None),
                gr.update(value=plot, visible=plot is not None)
            )
        
        def on_init():
            status, success = initialize_model()
            return status
        
        # Buton bağlantıları
        classify_btn.click(
            fn=on_classify,
            inputs=[image_input],
            outputs=[result_output, detailed_output, plot_output]
        )
        
        init_btn.click(
            fn=on_init,
            outputs=[model_status]
        )
        
        # Başlangıçta modeli yükle
        demo.load(
            fn=on_init,
            outputs=[model_status]
        )
    
    return demo

if __name__ == "__main__":
    print("🔬 Mineral Sınıflandırma Web Arayüzü Başlatılıyor...")
    print("📍 Tarayıcınızda otomatik olarak açılacak")
    print("🛑 Uygulamayı durdurmak için Ctrl+C basın")
    
    # Arayüzü oluştur ve başlat
    app = create_interface()
    app.launch(
        debug=False,
        share=False,
        inbrowser=True,
        server_name="127.0.0.1",
        server_port=7860
    ) 