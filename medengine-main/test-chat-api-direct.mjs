// Test the chat API directly using curl-like fetch
const testChatAPI = async () => {
  try {
    console.log('🔥 Testing Chat API directly...');
    
    const response = await fetch('http://localhost:3000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: 'Hello, this is a test message for MedEngine AI',
        conversationHistory: [],
      }),
    });
    
    console.log('📡 Response status:', response.status);
    console.log('📡 Response headers:', Object.fromEntries(response.headers));
    
    const data = await response.json();
    console.log('📝 Response data:', data);
    
    if (data.success) {
      console.log('✅ Chat API is working!');
      console.log('🤖 AI Response:', data.message);
    } else {
      console.log('❌ Chat API error:', data);
    }
    
  } catch (error) {
    console.error('❌ Test error:', error);
  }
};

// Run the test
testChatAPI();
