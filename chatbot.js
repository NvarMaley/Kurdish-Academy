// Kurdish Academy Chatbot - Simple Version
class KurdishChatbot {
    constructor() {
        this.isOpen = false;
        this.responses = {
            // Greetings
            'hello': 'Silav! How can I help you learn Kurdish today? 🌟',
            'hi': 'Merheba! What would you like to know about Kurdish? 😊',
            'hey': 'Silav! I\'m here to help with your Kurdish learning! 📚',
            
            // Grammar questions
            'grammar': 'I can help with Kurdish grammar! Try asking about: verbs, cases, pronouns, tenses, or gender.',
            'verb': 'Kurdish verbs change based on tense and person. Which tense would you like to learn about? (present, past, future)',
            'case': 'Kurdish has two main cases: direct (nominative) and oblique. The oblique case is used with prepositions and as the object of transitive verbs in the past tense.',
            'gender': 'Kurdish has masculine and feminine genders. Masculine nouns often end in consonants, while feminine nouns often end in -e or -a.',
            'tense': 'Kurdish has several tenses: present (niha), past simple (borî), future (pêşerojê), and more. Which one interests you?',
            
            // Alphabet
            'alphabet': 'The Kurdish alphabet has 31 letters in Kurmanci (Latin script) and uses Arabic script in Sorani. Would you like to practice?',
            'letter': 'Kurdish letters include special characters like ç, ê, î, ş, û. Check the Alfabê section for details!',
            
            // Vocabulary
            'vocabulary': 'I can help with vocabulary! Try asking about: family, colors, numbers, food, animals, or greetings.',
            'family': 'Family words: dê (mother), bav (father), bira (brother), xwişk (sister), malbat (family)',
            'color': 'Colors: sor (red), kesk (green), şîn (blue), zer (yellow), reş (black), spî (white)',
            'number': 'Numbers: yek (1), du (2), sê (3), çar (4), pênc (5), şeş (6), heft (7), heşt (8), neh (9), deh (10)',
            'food': 'Food words: nan (bread), av (water), çay (tea), xwarin (food), mêwe (fruit), sebze (vegetable)',
            'animal': 'Animals: se (dog), pisîk (cat), hesp (horse), beran (sheep), çêlek (bird), mase (fish)',
            
            // Greetings
            'greeting': 'Common greetings: Silav (Hello), Merheba (Hi), Spas (Thanks), Bi xêr hatî (Welcome), Xatirê te (Goodbye)',
            
            // Levels
            'level': 'We have 6 levels: A1 (Beginner), A2 (Elementary), B1 (Intermediate), B2 (Upper Intermediate), C1 (Advanced), C2 (Mastery). Which level are you?',
            'a1': 'A1 is for absolute beginners. You\'ll learn the alphabet, basic greetings, numbers, and simple phrases.',
            'a2': 'A2 focuses on simple conversations, daily routines, and basic grammar structures.',
            'b1': 'B1 covers culture, advanced grammar, and helps you become more autonomous in Kurdish.',
            'b2': 'B2 includes debates, literature, and complex text comprehension.',
            'c1': 'C1 is advanced level with academic texts, philosophy, and sophisticated expression.',
            'c2': 'C2 is mastery level covering poetry, translation, and complete fluency.',
            
            // Practice
            'practice': 'Practice makes perfect! Try the exercises in each course, or ask me to quiz you on vocabulary or grammar.',
            'exercise': 'Each course has practice exercises. Complete them to reinforce your learning!',
            
            // Translation
            'translate': 'I can help with simple translations! Try: "How do you say [word] in Kurdish?"',
            
            // Help
            'help': 'I can answer questions about: grammar, vocabulary, alphabet, levels, practice, and Kurdish culture. Just ask! 😊',
            'course': 'Our courses are organized in 6 levels (A1-C2) with 12 courses each. Click on a level to start learning!',
            
            // Default responses
            'default': [
                'Interesting question! Could you be more specific? Try asking about grammar, vocabulary, or levels.',
                'I\'m not sure I understand. Try asking about: verbs, cases, alphabet, or vocabulary topics.',
                'Hmm, I need more details. What aspect of Kurdish would you like to learn about?'
            ]
        };
        
        this.init();
    }
    
    init() {
        this.createChatWidget();
        this.attachEventListeners();
    }
    
    createChatWidget() {
        const chatHTML = `
            <div id="kurdish-chatbot" class="chatbot-container">
                <div class="chatbot-header" id="chat-header">
                    <div class="chatbot-title">
                        <span class="chatbot-icon">🤖</span>
                        <span>Kurdish Learning Assistant</span>
                    </div>
                    <button class="chatbot-close" id="chat-close">×</button>
                </div>
                <div class="chatbot-messages" id="chat-messages">
                    <div class="bot-message">
                        <strong>Bot:</strong> Silav! 👋 I'm your Kurdish learning assistant. Ask me anything about Kurdish grammar, vocabulary, or courses!
                    </div>
                </div>
                <div class="chatbot-input-container">
                    <input type="text" id="chat-input" class="chatbot-input" placeholder="Type your question...">
                    <button id="chat-send" class="chatbot-send">Send</button>
                </div>
            </div>
            <button id="chat-toggle" class="chatbot-toggle">
                💬
            </button>
        `;
        
        document.body.insertAdjacentHTML('beforeend', chatHTML);
    }
    
    attachEventListeners() {
        const toggleBtn = document.getElementById('chat-toggle');
        const closeBtn = document.getElementById('chat-close');
        const sendBtn = document.getElementById('chat-send');
        const input = document.getElementById('chat-input');
        const chatContainer = document.getElementById('kurdish-chatbot');
        
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
    
    sendMessage() {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        
        if (!message) return;
        
        this.addMessage(message, 'user');
        input.value = '';
        
        setTimeout(() => {
            const response = this.getResponse(message);
            this.addMessage(response, 'bot');
        }, 500);
    }
    
    addMessage(text, sender) {
        const messagesContainer = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = sender === 'user' ? 'user-message' : 'bot-message';
        messageDiv.innerHTML = `<strong>${sender === 'user' ? 'You' : 'Bot'}:</strong> ${text}`;
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    getResponse(message) {
        const lowerMessage = message.toLowerCase();
        
        // Check for exact matches first
        for (const [key, response] of Object.entries(this.responses)) {
            if (key !== 'default' && lowerMessage.includes(key)) {
                return response;
            }
        }
        
        // Enhanced pattern matching for more questions
        
        // Translation requests
        if (lowerMessage.includes('how do you say') || lowerMessage.includes('translate') || lowerMessage.includes('what is') || lowerMessage.includes('mean')) {
            return 'I can help with translations! Try asking about specific topics like: family words, colors, numbers, greetings, food, animals, or body parts. Or visit our Vocabulary (Peyvên) section for comprehensive lists!';
        }
        
        // Learning questions
        if (lowerMessage.includes('learn') || lowerMessage.includes('start') || lowerMessage.includes('begin')) {
            return 'Great! Start with Level A1 (Destpêk) to learn the alphabet, basic greetings, and numbers. Each level has 12 progressive courses. Click on the yellow A1 bubble to begin! 🌟';
        }
        
        // Difficulty questions
        if (lowerMessage.includes('difficult') || lowerMessage.includes('hard') || lowerMessage.includes('easy')) {
            return 'Kurdish can be challenging but very rewarding! The ergativity and case system are unique. Start with A1 basics and progress gradually. Practice daily for best results! 💪';
        }
        
        // Time questions
        if (lowerMessage.includes('how long') || lowerMessage.includes('time')) {
            return 'Learning Kurdish takes dedication! Expect 6-12 months for basic fluency (A1-A2), 1-2 years for intermediate (B1-B2), and 2-3+ years for advanced levels (C1-C2). Practice consistently! ⏰';
        }
        
        // Pronunciation questions
        if (lowerMessage.includes('pronounce') || lowerMessage.includes('pronunciation') || lowerMessage.includes('sound')) {
            return 'Kurdish pronunciation includes special sounds like ç (ch), ê (long e), î (long i), ş (sh), û (long u). Check our Alfabê section for audio examples and practice! 🔊';
        }
        
        // Writing questions
        if (lowerMessage.includes('write') || lowerMessage.includes('writing') || lowerMessage.includes('script')) {
            return 'Kurmanci uses Latin script (31 letters), while Sorani uses Arabic script. Start with the alphabet in our Alfabê section, then practice in Nivîsandin (Writing) exercises! ✍️';
        }
        
        // Speaking questions
        if (lowerMessage.includes('speak') || lowerMessage.includes('speaking') || lowerMessage.includes('conversation')) {
            return 'Practice speaking from day one! Start with greetings (Silav, Merheba), then simple phrases. Our Axaftin (Speaking) section has dialogues and pronunciation guides! 🗣️';
        }
        
        // Listening questions
        if (lowerMessage.includes('listen') || lowerMessage.includes('listening') || lowerMessage.includes('hear')) {
            return 'Listening is crucial! Check our Guhdarîkirin (Listening) section for audio exercises, dialogues, and Kurdish media recommendations. Immerse yourself! 👂';
        }
        
        // Reading questions
        if (lowerMessage.includes('read') || lowerMessage.includes('reading') || lowerMessage.includes('text')) {
            return 'Start reading simple texts in A1-A2, then progress to stories and articles. Our Xwendin (Reading) section has graded texts for all levels! 📖';
        }
        
        // Dialect questions
        if (lowerMessage.includes('dialect') || lowerMessage.includes('kurmanci') || lowerMessage.includes('sorani') || lowerMessage.includes('difference')) {
            return 'Kurdish has two main dialects: Kurmanci (Northern, Latin script) and Sorani (Central, Arabic script). We teach both! Kurmanci is spoken in Turkey, Syria, and parts of Iraq/Iran. Sorani is spoken in Iraq and Iran. 🗺️';
        }
        
        // Culture questions
        if (lowerMessage.includes('culture') || lowerMessage.includes('tradition') || lowerMessage.includes('history')) {
            return 'Kurdish culture is rich and ancient! Explore our Culture section for history, music, dance, literature, and traditions. Understanding culture enhances language learning! 🎭';
        }
        
        // Resources questions
        if (lowerMessage.includes('resource') || lowerMessage.includes('book') || lowerMessage.includes('app') || lowerMessage.includes('recommend')) {
            return 'Kurdish Academy has everything you need! Use our structured courses (A1-C2), practice sections (Vocabulary, Grammar, Verbs), and skill exercises (Listening, Reading, Writing, Speaking). Study 30 min daily! 📚';
        }
        
        // Motivation questions
        if (lowerMessage.includes('motivat') || lowerMessage.includes('give up') || lowerMessage.includes('discourag')) {
            return 'Don\'t give up! Every polyglot started as a beginner. Kurdish is a beautiful language worth learning. Set small goals, celebrate progress, and practice daily. You can do this! 🌟💪';
        }
        
        // Specific grammar topics
        if (lowerMessage.includes('ergative') || lowerMessage.includes('ergativity')) {
            return 'Kurdish uses split ergativity! In past transitive sentences, the subject takes the oblique case and the verb agrees with the object. Example: "Min (I-oblique) kitêb (book) dît (saw-3sg)". It\'s unique but logical! 🧠';
        }
        
        if (lowerMessage.includes('plural') || lowerMessage.includes('plurals')) {
            return 'Kurdish plurals: Add -an for most nouns (kitêb → kitêban), -în for some (zarok → zarokîn), or use irregular forms. Feminine nouns ending in -e change to -ên (xanî → xanîn). Check Grammar section! 📝';
        }
        
        if (lowerMessage.includes('adjective')) {
            return 'Kurdish adjectives usually come after nouns: "kitêba mezin" (big book). They don\'t change for gender or number. Comparatives use "ji...tir" (more than). Check Rêziman (Grammar)! 📏';
        }
        
        if (lowerMessage.includes('preposition')) {
            return 'Common Kurdish prepositions: li (at/in), ji (from), bo (for), bi (with), di (in). They require the oblique case! Example: "li malê" (at home-oblique). Practice in Grammar section! 🎯';
        }
        
        // Thank you responses
        if (lowerMessage.includes('thank') || lowerMessage.includes('spas') || lowerMessage.includes('merci')) {
            return 'Tu bi xêr hatî! (You\'re welcome!) Keep up the great work learning Kurdish! 😊🌟';
        }
        
        // Goodbye responses
        if (lowerMessage.includes('bye') || lowerMessage.includes('goodbye') || lowerMessage.includes('see you')) {
            return 'Bi xatirê te! (Goodbye!) Come back anytime you need help with Kurdish. Happy learning! �';
        }
        
        // Questions about the chatbot itself
        if (lowerMessage.includes('who are you') || lowerMessage.includes('what are you') || lowerMessage.includes('your name')) {
            return 'I\'m the Kurdish Academy Learning Assistant! 🤖 I\'m here to help you learn Kurdish by answering questions about grammar, vocabulary, courses, and more. Ask me anything! 💚';
        }
        
        // Catch-all for questions
        if (lowerMessage.includes('?') || lowerMessage.includes('what') || lowerMessage.includes('how') || lowerMessage.includes('why') || lowerMessage.includes('when') || lowerMessage.includes('where')) {
            return 'Great question! I can help with: 📚 Grammar (verbs, cases, tenses), 📖 Vocabulary (family, colors, numbers), 🎓 Levels (A1-C2), 💬 Skills (speaking, listening, reading, writing), 🗺️ Dialects (Kurmanci vs Sorani), and 🎭 Culture. What would you like to know more about?';
        }
        
        // Return random default response
        const defaults = this.responses.default;
        return defaults[Math.floor(Math.random() * defaults.length)];
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new KurdishChatbot();
});
