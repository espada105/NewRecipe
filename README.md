# NewRecipe 🍽️

## Innovative AI-Powered Culinary Assistant

![Cooking App Interface](https://github.com/user-attachments/assets/f9d48386-1f5e-4cec-b295-3facaa42d186)

NewRecipe is an innovative recipe discovery platform leveraging **Llama3.1-8B** with **Unsloth** optimization technology. This multimodal solution offers various ways to discover and create delicious recipes tailored to your needs.

## 🌟 Key Features

### 📸 Image Recognition Recipe Search
Upload a photo of your ingredients and our CLIP vision model automatically identifies them, suggesting perfect recipes based on what you have. No more wondering what to cook with the ingredients in your refrigerator!

### ⌨️ Text-Based Recipe Search
Enter your desired ingredients or dish name as text, and receive detailed cooking instructions. Try natural language queries like "What can I make with onions and eggs?"

### 🎙️ Voice Recognition Recipe Search
When your hands are busy cooking, just ask using your voice! Our system powered by Google Cloud Speech-to-Text API lets you inquire about next steps without stopping to wash your hands.

## 🛠️ Technology Stack

- **Base Model**: Llama3.1-8B + Unsloth optimization (2x speed improvement)
- **Training Data**: AdamCodd/recipe-nlg-alpaca
- **Image Recognition**: CLIP (Contrastive Language-Image Pre-training)
- **Voice Processing**: Google Cloud Speech-to-Text API
- **Model Evaluation**: BLEU and ROUGE score measurements

## 💡 Optimization & Performance

- **LoRA Fine-tuning**: Efficiently updating only 1-10% of parameters
- **4-bit Quantization**: Reduced memory usage and improved inference speed
- **Unsloth Acceleration**: 2x faster training and inference compared to baseline
- **Multimodal Input Support**: Various input methods including text, images, and voice

## 🚀 How to Use

### Finding Recipes with Images
1. Upload a photo of your ingredients
2. The CLIP model automatically recognizes the ingredients
3. A customized recipe is generated based on the identified ingredients

### Finding Recipes with Text
```
Question: Tell me a tomato pasta recipe
Response: [Tomato Pasta]
[INGREDIENTS]
onion, tomato paste, olive oil, parsley, salt, tomato, pasta, oregano, 
basil, garlic, parmesan cheese, pepper

[DIRECTIONS]:
- Boil water for pasta. Cook according to directions
- Meanwhile, saute onion and garlic in olive oil until onion is translucent
...
```

### Finding Recipes with Voice
- Voice recognition requires a separate Google Cloud Speech-to-Text API authentication file
- Refer to the provided code to set up the voice recognition module

---

*NewRecipe: Let AI be your kitchen assistant*
