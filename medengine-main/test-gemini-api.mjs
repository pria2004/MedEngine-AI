import { GoogleGenerativeAI } from '@google/generative-ai';

// Test script to verify Gemini API key
const testGeminiAPI = async () => {
  const apiKey = 'AIzaSyDYTBYrmHfWaEq4a5C-G37lLwVMXO7anHY';
  
  try {
    console.log('🔑 Testing Gemini API key...');
    
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ 
      model: 'gemini-1.5-flash',
      generationConfig: {
        temperature: 0.7,
        topP: 0.8,
        topK: 40,
        maxOutputTokens: 100,
      },
    });
    
    const prompt = 'Hello, can you say "API connection successful"?';
    console.log('📤 Sending test prompt:', prompt);
    
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    
    console.log('✅ API Response:', text);
    console.log('🎉 Gemini API is working correctly!');
    
  } catch (error) {
    console.error('❌ Gemini API Error:', error);
    console.error('❌ Error details:', error.message);
  }
};

testGeminiAPI();
