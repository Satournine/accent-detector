from speechbrain.pretrained.interfaces import Pretrained

class CustomEncoderWav2vec2Classifier(Pretrained):
    MODULES_NEEDED = ["model", "encoder", "mean_var_norm"]
    HPARAMS_NEEDED = ["label_encoder"]
