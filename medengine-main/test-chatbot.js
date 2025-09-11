// Simple test script to verify chatbot API connection
const testChatbot = async () => {
  try {
    console.log('Testing MedEngine AI Chatbot API...');
    
    const response = await fetch('http://localhost:3000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: 'Hello, can you help me with general health information?',
        conversationHistory: [],
      }),
    });

    const data = await response.json();
    
    console.log('✅ API Response Status:', response.status);
    console.log('✅ API Response:', data);
    
    if (data.success) {
      console.log('🎉 Chatbot is working correctly!');
      console.log('📝 AI Response:', data.message);
    } else {
      console.log('❌ Chatbot API error:', data.error);
    }
  } catch (error) {
    console.error('❌ Network or connection error:', error.message);
  }
};

// Wait a moment for the server to be ready, then test
setTimeout(testChatbot, 3000);
