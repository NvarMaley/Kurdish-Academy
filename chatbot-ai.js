// Kurdish Academy AI Chatbot - Real AI with Gemini API
class KurdishAIChatbot {
    constructor() {
        this.isOpen = false;
        this.apiKey = ''; // User will need to add their free API key
        this.useAPI = false; // Set to true when API key is added
        this.conversationHistory = [];
        
        // Fallback responses for when API is not available
        this.fallbackResponses = {
            'hello': 'Silav! I\'m your AI assistant. I can answer any question! Ask me about Kurdish, or anything else! 🤖',
            'hi': 'Merheba! I\'m a real AI assistant. What would you like to know? 😊',
            'help': 'I\'m an AI assistant that can answer ANY question - about Kurdish, science, history, math, cooking, or anything else! Just ask! 💡',
            'default': 'I can answer any question you have! Try asking me about Kurdish language, grammar, culture, or anything else that interests you. 🌟'
        };
        
        this.init();
    }
    
    init() {
        this.createChatWidget();
        this.attachEventListeners();
        this.checkAPIKey();
    }
    
    checkAPIKey() {
        // Check if API key is stored in localStorage
        const storedKey = localStorage.getItem('gemini_api_key');
        if (storedKey && storedKey.length > 0) {
            this.apiKey = storedKey;
            this.useAPI = true;
        }
    }
    
    createChatWidget() {
        const chatHTML = `
            <div id="kurdish-chatbot" class="chatbot-container">
                <div class="chatbot-header" id="chat-header">
                    <div class="chatbot-title">
                        <span class="chatbot-icon">🤖</span>
                        <span>Kurdish Academy AI Assistant</span>
                        <span class="ai-badge">✨ AI</span>
                    </div>
                    <button class="chatbot-close" id="chat-close">×</button>
                </div>
                <div class="chatbot-messages" id="chat-messages">
                    <div class="bot-message">
                        <strong>AI Assistant:</strong> Silav! 👋 I'm your AI assistant. I can answer ANY question - about Kurdish language, grammar, culture, or anything else in the world! Ask me anything! 🌍
                    </div>
                    ${!this.useAPI ? `
                    <div class="bot-message api-notice">
                        <strong>💡 Pro Tip:</strong> For full AI capabilities, add your free Google Gemini API key. Type "setup api" to get started!
                    </div>
                    ` : ''}
                </div>
                <div class="chatbot-input-container">
                    <input type="text" id="chat-input" class="chatbot-input" placeholder="Ask me anything...">
                    <button id="chat-send" class="chatbot-send">
                        <span class="send-icon">➤</span>
                    </button>
                </div>
            </div>
            <button id="chat-toggle" class="chatbot-toggle">
                <span class="toggle-icon">💬</span>
                <span class="ai-indicator">AI</span>
            </button>
        `;
        
        document.body.insertAdjacentHTML('beforeend', chatHTML);
    }
    
    attachEventListeners() {
        const toggleBtn = document.getElementById('chat-toggle');
        const closeBtn = document.getElementById('chat-close');
        const sendBtn = document.getElementById('chat-send');
        const input = document.getElementById('chat-input');
        
        toggleBtn.addEventListener('click', () => this.toggleChat());
        closeBtn.addEventListener('click', () => this.toggleChat());
        sendBtn.addEventListener('click', () => this.sendMessage());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });
    }
    
    toggleChat() {
        this.isOpen = !this.isOpen;
        const chatContainer = document.getElementById('kurdish-chatbot');
        const toggleBtn = document.getElementById('chat-toggle');
        
        if (this.isOpen) {
            chatContainer.style.display = 'flex';
            toggleBtn.style.display = 'none';
        } else {
            chatContainer.style.display = 'none';
            toggleBtn.style.display = 'flex';
        }
    }
    
    async sendMessage() {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        
        if (!message) return;
        
        // Check for API setup command
        if (message.toLowerCase().includes('setup api') || message.toLowerCase().includes('api key')) {
            this.showAPISetup();
            input.value = '';
            return;
        }
        
        this.addMessage(message, 'user');
        input.value = '';
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            let response;
            if (this.useAPI && this.apiKey) {
                response = await this.getAIResponse(message);
            } else {
                response = await this.getSmartFallbackResponse(message);
            }
            
            this.removeTypingIndicator();
            this.addMessage(response, 'bot');
        } catch (error) {
            this.removeTypingIndicator();
            this.addMessage('Sorry, I encountered an error. Please try again! 😅', 'bot');
        }
    }
    
    showTypingIndicator() {
        const messagesContainer = document.getElementById('chat-messages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'bot-message typing-indicator';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = '<span class="dot"></span><span class="dot"></span><span class="dot"></span>';
        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    removeTypingIndicator() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) indicator.remove();
    }
    
    async getAIResponse(message) {
        console.log('🤖 Using AI API to respond...');
        console.log('API Key exists:', !!this.apiKey);
        console.log('API Key length:', this.apiKey ? this.apiKey.length : 0);
        
        // Add Kurdish learning context to the prompt
        const systemPrompt = `You are a helpful AI assistant for Kurdish Academy, a Kurdish language learning platform. 
You can answer ANY question, but you have special expertise in:
- Kurdish language (Kurmanci and Sorani dialects)
- Kurdish grammar, vocabulary, and pronunciation
- Kurdish culture, history, and traditions
- Language learning tips and strategies

When answering Kurdish-related questions, be detailed and educational. For other topics, answer normally as a helpful AI assistant.
Keep responses concise (2-3 sentences for simple questions, more for complex ones).`;

        const fullPrompt = `${systemPrompt}\n\nUser question: ${message}`;
        
        try {
            // Using Gemini API (free tier)
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${this.apiKey}`;
            console.log('Making API request...');
            
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    contents: [{
                        parts: [{
                            text: fullPrompt
                        }]
                    }]
                })
            });
            
            console.log('API Response status:', response.status);
            
            if (!response.ok) {
                const errorData = await response.json();
                console.error('API Error details:', errorData);
                throw new Error(`API request failed: ${response.status}`);
            }
            
            const data = await response.json();
            console.log('✅ AI Response received!');
            return data.candidates[0].content.parts[0].text;
            
        } catch (error) {
            console.error('❌ API Error:', error);
            this.addMessage('⚠️ API error occurred. Using fallback responses. Check console for details.', 'bot');
            return this.getSmartFallbackResponse(message);
        }
    }
    
    async getSmartFallbackResponse(message) {
        const lowerMessage = message.toLowerCase();
        
        // Simulate thinking delay
        await new Promise(resolve => setTimeout(resolve, 800));
        
        // Kurdish-specific responses
        if (lowerMessage.includes('kurdish') || lowerMessage.includes('kurde') || lowerMessage.includes('kurmanci') || lowerMessage.includes('sorani')) {
            if (lowerMessage.includes('learn') || lowerMessage.includes('start')) {
                return 'To learn Kurdish, start with our A1 level courses! You\'ll learn the alphabet, basic greetings, and essential vocabulary. Kurdish has two main dialects: Kurmanci (Latin script) and Sorani (Arabic script). We teach both! Click on the yellow A1 bubble to begin your journey! 🌟';
            }
            if (lowerMessage.includes('difficult') || lowerMessage.includes('hard')) {
                return 'Kurdish has unique features like ergativity and the oblique case system, which can be challenging. However, with consistent practice, it becomes logical! Start with basics (A1-A2) and progress gradually. The grammar is actually quite regular once you understand the patterns. 💪';
            }
            if (lowerMessage.includes('grammar')) {
                return 'Kurdish grammar includes: 2 genders (masculine/feminine), 2 cases (direct/oblique), split ergativity in past tense, and verb conjugations. Check our Rêziman (Grammar) section for detailed lessons on each topic! 📚';
            }
            return 'Kurdish is a beautiful Indo-European language with rich history! We offer comprehensive courses from A1 (beginner) to C2 (mastery). Explore our sections: Alphabet, Vocabulary, Verbs, Grammar, and practice your skills in Listening, Reading, Writing, and Speaking! 🎓';
        }
        
        // General knowledge responses
        if (lowerMessage.includes('hello') || lowerMessage.includes('hi') || lowerMessage.includes('hey')) {
            return 'Silav! 👋 I\'m your AI assistant. I can answer questions about Kurdish language, culture, grammar, or ANY other topic! What would you like to know? 🌍';
        }
        
        if (lowerMessage.includes('who are you') || lowerMessage.includes('what are you')) {
            return 'I\'m an AI assistant for Kurdish Academy! 🤖 I can help with Kurdish language learning AND answer general questions about any topic. I\'m here to make your learning journey easier and more fun! Ask me anything! 💚';
        }
        
        if (lowerMessage.includes('thank')) {
            return 'Tu bi xêr hatî! (You\'re welcome!) Happy to help anytime! 😊✨';
        }
        
        if (lowerMessage.includes('help')) {
            return 'I can help with: 📚 Kurdish language (grammar, vocabulary, pronunciation), 🎓 Learning tips, 🗺️ Kurdish culture & history, 🌍 General knowledge (science, math, history, etc.), 💬 Conversation practice. What interests you? 🤔';
        }
        
        // For questions we can't answer specifically
        if (lowerMessage.includes('?') || lowerMessage.includes('what') || lowerMessage.includes('how') || lowerMessage.includes('why')) {
            if (!this.useAPI) {
                return 'That\'s an interesting question! While I can provide basic information, for the most accurate and detailed answers, I recommend adding a free Google Gemini API key (type "setup api"). For Kurdish-related questions, I can help right away! What specifically about Kurdish would you like to know? 🤓';
            } else {
                return 'I\'m working on that question! My AI capabilities are active. For the best answers on any topic, I\'m here to help. For Kurdish-specific questions, I have extensive knowledge! 🌟';
            }
        }
        
        return 'I\'m here to help! I specialize in Kurdish language learning, but I can discuss many topics. Try asking me about: Kurdish grammar, vocabulary, culture, or any learning questions you have! 🌟';
    }
    
    showAPISetup() {
        const setupMessage = `
            <strong>🔑 Setup Free AI (Google Gemini):</strong><br><br>
            1. Visit: <a href="https://makersuite.google.com/app/apikey" target="_blank">Google AI Studio</a><br>
            2. Click "Create API Key"<br>
            3. Copy your free API key<br>
            4. Paste it here in chat<br><br>
            <small>Your key is stored locally and never shared. Free tier: 60 requests/minute! 🚀</small>
        `;
        
        this.addMessage(setupMessage, 'bot');
        
        // Listen for API key input
        const input = document.getElementById('chat-input');
        const originalPlaceholder = input.placeholder;
        input.placeholder = 'Paste your API key here...';
        
        const keyHandler = (e) => {
            if (e.key === 'Enter') {
                const key = input.value.trim();
                if (key.startsWith('AIza') && key.length > 30) {
                    localStorage.setItem('gemini_api_key', key);
                    this.apiKey = key;
                    this.useAPI = true;
                    input.value = '';
                    input.placeholder = originalPlaceholder;
                    this.addMessage('✅ API key saved! I\'m now powered by real AI and can answer ANY question! Try asking me something! 🚀', 'bot');
                    input.removeEventListener('keypress', keyHandler);
                } else if (key.length > 0) {
                    this.addMessage('❌ Invalid API key format. It should start with "AIza". Try again or type "setup api" for instructions.', 'bot');
                    input.value = '';
                }
            }
        };
        
        input.addEventListener('keypress', keyHandler);
    }
    
    addMessage(text, sender) {
        const messagesContainer = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = sender === 'user' ? 'user-message' : 'bot-message';
        messageDiv.innerHTML = `<strong>${sender === 'user' ? 'You' : 'AI Assistant'}:</strong> ${text}`;
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
}

// Initialize AI chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new KurdishAIChatbot();
});
