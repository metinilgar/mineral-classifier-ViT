"""
Mineral sınıflandırma modeli yükleyici modülü
"""
import torch
from transformers import ViTForImageClassification, ViTImageProcessor
from typing import Tuple
import os

class MineralClassifier:
    """Mineral sınıflandırma modeli sınıfı"""
    
    def __init__(self, model_path: str = "./model"):
        """
        Model yükleyici başlatıcı
        
        Args:
            model_path (str): Model dosyalarının bulunduğu dizin yolu
        """
        self.model_path = model_path
        self.model = None
        self.processor = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.is_loaded = False
        
    def load_model(self) -> bool:
        """
        Modeli ve işleyiciyi yükle
        
        Returns:
            bool: Yükleme başarılı ise True
        """
        try:
            print(f"Model yükleniyor: {self.model_path}")
            print(f"Kullanılan cihaz: {self.device}")
            
            # Model ve processor yükleme
            self.model = ViTForImageClassification.from_pretrained(self.model_path)
            self.processor = ViTImageProcessor.from_pretrained(self.model_path)
            
            # Modeli cihaza taşı
            self.model.to(self.device)
            self.model.eval()
            
            self.is_loaded = True
            print("Model başarıyla yüklendi!")
            return True
            
        except Exception as e:
            print(f"Model yükleme hatası: {str(e)}")
            return False
    
    def predict(self, image) -> Tuple[str, float, dict]:
        """
        Görüntü üzerinde tahmin yap
        
        Args:
            image: PIL Image objesi
            
        Returns:
            Tuple[str, float, dict]: (tahmin_edilen_sınıf, güven_skoru, tüm_skorlar)
        """
        if not self.is_loaded:
            raise ValueError("Model henüz yüklenmedi! Önce load_model() metodunu çağırın.")
        
        try:
            # Görüntüyü işle
            inputs = self.processor(images=image, return_tensors="pt")
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # Tahmin yap
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                
                # Softmax uygula (olasılık dağılımı için)
                probabilities = torch.nn.functional.softmax(logits, dim=-1)
                
                # En yüksek skorlu sınıfı bul
                predicted_idx = logits.argmax(-1).item()
                confidence = probabilities[0][predicted_idx].item()
                
                # Tüm sınıf skorlarını al
                all_scores = {}
                for idx, prob in enumerate(probabilities[0]):
                    label = self.model.config.id2label[idx]
                    all_scores[label] = prob.item()
                
                predicted_label = self.model.config.id2label[predicted_idx]
                
                return predicted_label, confidence, all_scores
                
        except Exception as e:
            raise Exception(f"Tahmin hatası: {str(e)}")
    
    def get_class_names(self) -> list:
        """
        Sınıf isimlerini döndür
        
        Returns:
            list: Sınıf isimleri listesi
        """
        if not self.is_loaded:
            return []
        return list(self.model.config.id2label.values())

# Global model instance
_classifier_instance = None

def get_classifier(model_path: str = "./model") -> MineralClassifier:
    """
    Singleton pattern ile classifier instance döndür
    
    Args:
        model_path (str): Model dizin yolu
        
    Returns:
        MineralClassifier: Classifier instance
    """
    global _classifier_instance
    if _classifier_instance is None:
        _classifier_instance = MineralClassifier(model_path)
    return _classifier_instance 