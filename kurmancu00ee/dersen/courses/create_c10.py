# Script to complete Course 10
import re

# Read the current file
with open('course-10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The file already has Section 1 (vocabulary) updated correctly
# We need to update sections 2-8 and JavaScript

# Find where Section 2 starts and replace everything after Section 1
section1_end = content.find('</div>\n\n            <div class="section">\n                <h2 class="section-title"><span class="section-icon">🧠</span>2.')

if section1_end > 0:
    # Keep everything up to end of Section 1
    new_content = content[:section1_end + 6]  # +6 for '</div>'
    
    # Add the rest of the course (sections 2-8, completion, JavaScript)
    new_content += '''

            <!-- Section 2: Structure -->
            <div class="section">
                <h2 class="section-title"><span class="section-icon">🧠</span>2. Struktur: Dates & Time Expressions</h2>
                <p style="font-size: 1.1rem; margin-bottom: 20px;">Learn how to express dates and time in Kurdish:</p>
                
                <div class="structure-box">
                    <h3 style="color: #f9a825; margin-bottom: 15px;">💡 Saying Dates</h3>
                    <div class="structure-pattern">
                        <strong style="color: #f57f17;">Pattern:</strong> [Day number] + [Month name]<br><br>
                        <strong>Examples:</strong><br>
                        • <strong style="color: #1976d2;">21 Adar</strong> = March 21 (Newroz!)<br>
                        • <strong style="color: #1976d2;">1 Rêbendan</strong> = January 1<br>
                        • <strong style="color: #1976d2;">15 Gulan</strong> = May 15
                    </div>
                </div>

                <div class="structure-box">
                    <h3 style="color: #f9a825; margin-bottom: 15px;">💡 Time Expressions</h3>
                    <div class="structure-pattern">
                        <strong>Îro:</strong> Today<br>
                        • <strong style="color: #388e3c;">Îro</strong> Duşem e. = Today is Monday.<br><br>
                        
                        <strong>Sibe:</strong> Tomorrow<br>
                        • <strong style="color: #388e3c;">Sibe</strong> ez diçim dibistanê. = Tomorrow I go to school.<br><br>
                        
                        <strong>Duh:</strong> Yesterday<br>
                        • <strong style="color: #388e3c;">Duh</strong> ez li malê bûm. = Yesterday I was at home.
                    </div>
                </div>

                <div class="exercise-box">
                    <div class="exercise-title">🎯 Practice: Complete the Sentences</div>
                    <p style="margin-bottom: 15px; color: #666;">Fill in with the correct time word:</p>
                    
                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">1. ___ Duşem e. (Today is Monday)</label>
                        <input type="text" id="time-q1" placeholder="Type îro, sibe, or duh...">
                        <div id="time-q1-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">2. ___ ez diçim malê. (Tomorrow I go home)</label>
                        <input type="text" id="time-q2" placeholder="Type îro, sibe, or duh...">
                        <div id="time-q2-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">3. ___ em li parkan bûn. (Yesterday we were at the park)</label>
                        <input type="text" id="time-q3" placeholder="Type îro, sibe, or duh...">
                        <div id="time-q3-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <button onclick="checkTimeWords()">✓ Check Answers</button>
                    <div id="time-score" style="margin-top: 15px; font-size: 1.2rem; font-weight: bold;"></div>
                </div>
            </div>

            <!-- Section 3: Listening -->
            <div class="section">
                <h2 class="section-title"><span class="section-icon">🎧</span>3. Guhdarîkirin (Listening): Making Plans</h2>
                <p style="font-size: 1.1rem; margin-bottom: 20px;">Listen to people talking about their schedules:</p>
                
                <div class="example-dialogue">
                    <h4 style="color: #f9a825; margin-bottom: 15px;">🎙️ Dialogue 1: Weekly Schedule</h4>
                    <div class="dialogue-line">
                        <div class="speaker">👤 Dîlan:</div>
                        <div class="kurdish-text"><strong style="color: #388e3c;">Îro</strong> çi roj e?<br>
                        <strong style="color: #388e3c;">Îro</strong> <strong style="color: #f9a825;">Duşem</strong> e.<br>
                        Ez <strong style="color: #1976d2;">her Duşem</strong> û <strong style="color: #1976d2;">Çarşem</strong> diçim zanîngehê.<br>
                        <strong style="color: #388e3c;">Sibe</strong> <strong style="color: #f9a825;">Sêşem</strong> e, ez li malê dimînim.<br>
                        <strong style="color: #f9a825;">Pêncşem</strong> û <strong style="color: #f9a825;">În</strong> ez dixebitim.<br>
                        <strong style="color: #f9a825;">Şemî</strong> û <strong style="color: #f9a825;">Yekşem</strong> ez bi hevalên xwe re derdikevim.</div>
                        <div class="translation">What day is today? Today is Monday. I go to university every Monday and Wednesday. Tomorrow is Tuesday, I stay at home. Thursday and Friday I work. Saturday and Sunday I go out with my friends.</div>
                    </div>
                </div>

                <div class="example-dialogue">
                    <h4 style="color: #f9a825; margin-bottom: 15px;">🎙️ Dialogue 2: Birthday Plans</h4>
                    <div class="dialogue-line">
                        <div class="speaker">👤 Rojîn:</div>
                        <div class="kurdish-text">Rojbûna min <strong style="color: #f9a825;">15 Gulan</strong> e.<br>
                        <strong style="color: #388e3c;">Îro</strong> <strong style="color: #f9a825;">10 Gulan</strong> e.<br>
                        <strong style="color: #388e3c;">Sibe</strong> ez diçim bazarê.<br>
                        Ez <strong style="color: #1976d2;">pir caran</strong> li mala xwe cejn dikim.<br>
                        Ez <strong style="color: #1976d2;">her sal</strong> bi malbata xwe re pîroz dikim.</div>
                        <div class="translation">My birthday is May 15. Today is May 10. Tomorrow I go to the market. I often celebrate at my house. I celebrate every year with my family.</div>
                    </div>
                </div>

                <div class="exercise-box">
                    <div class="exercise-title">🎯 Comprehension Questions</div>
                    <p style="margin-bottom: 15px;">Answer in Kurdish:</p>
                    
                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">1. What day is today in Dialogue 1?</label>
                        <input type="text" id="listen-q1" placeholder="Answer in Kurdish...">
                        <div id="listen-q1-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">2. When is Rojîn's birthday?</label>
                        <input type="text" id="listen-q2" placeholder="Answer in Kurdish...">
                        <div id="listen-q2-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <button onclick="checkListening()">✓ Check Answers</button>
                    <div id="listen-score" style="margin-top: 15px; font-size: 1.2rem; font-weight: bold;"></div>
                </div>
            </div>

            <!-- Section 4: Reading -->
            <div class="section">
                <h2 class="section-title"><span class="section-icon">📖</span>4. Xwendin (Reading): Kurdish Calendar & Newroz</h2>
                <p style="font-size: 1.1rem; margin-bottom: 20px;">Read about the Kurdish calendar and Newroz:</p>
                
                <div style="background: #fff9c4; padding: 25px; border-radius: 12px; margin: 20px 0; border-left: 5px solid #f9a825;">
                    <h4 style="color: #f57f17; margin-bottom: 15px;">📅 Salnameyê Kurdî (Kurdish Calendar)</h4>
                    <p style="font-size: 1.1rem; line-height: 2;">
                        Kurdan salnameyeke taybet heye.<br>
                        Sala Kurdî <span style="color: #f57f17; font-weight: bold;">21 Adar</span> dest pê dike.<br>
                        Ev roj <span style="color: #f57f17; font-weight: bold;">Newroz</span> e - cejna biharê ye.<br>
                        Newroz <span style="color: #1976d2; font-weight: bold;">her sal</span> <span style="color: #f57f17; font-weight: bold;">21 Adar</span> tê pîrozkirin.<br>
                        Ev cejna herî mezin a Kurdan e.
                    </p>
                </div>

                <div class="exercise-box">
                    <div class="exercise-title">🎯 Reading Comprehension</div>
                    <p style="margin-bottom: 20px; color: #666;">Answer these questions:</p>
                    
                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">1. When does the Kurdish year begin?</label>
                        <input type="text" id="read-q1" placeholder="Answer in Kurdish...">
                        <div id="read-q1-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">2. What is Newroz?</label>
                        <input type="text" id="read-q2" placeholder="Answer in Kurdish...">
                        <div id="read-q2-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <button onclick="checkReading()">✓ Check Answers</button>
                    <div id="read-score" style="margin-top: 15px; font-size: 1.2rem; font-weight: bold;"></div>
                </div>
            </div>

            <!-- Section 5: Writing -->
            <div class="section">
                <h2 class="section-title"><span class="section-icon">✍️</span>5. Nivîsandin (Writing): Your Schedule</h2>
                <div class="exercise-box">
                    <div class="exercise-title">📝 Writing Exercise: Your Week</div>
                    <p style="margin-bottom: 15px; color: #666;">Write about your weekly schedule using days and time words.</p>
                    
                    <textarea id="write-schedule" rows="8" placeholder="Example: Îro Çarşem e. Ez her Duşem diçim zanîngehê..."></textarea>
                    <div id="write-feedback" style="margin-top: 15px; font-weight: bold;"></div>
                    <button onclick="checkWriting()">✓ Submit</button>
                </div>
            </div>

            <!-- Section 6: Speaking -->
            <div class="section">
                <h2 class="section-title"><span class="section-icon">🗣️</span>6. Axaftin (Speaking): Today & Tomorrow</h2>
                <p style="font-size: 1.1rem; margin-bottom: 20px;">Practice talking about today and tomorrow:</p>
                <div class="exercise-box">
                    <div class="exercise-title">🎭 Speaking Scenarios</div>
                    
                    <div style="margin: 25px 0; padding: 20px; background: #fff9c4; border-radius: 10px;">
                        <h4 style="color: #f57f17; margin-bottom: 15px;">Scenario 1: Someone asks "Îro çi roj e?"</h4>
                        <p style="margin-bottom: 10px;"><strong>What do you say?</strong></p>
                        <div style="display: flex; flex-direction: column; gap: 10px;">
                            <button class="speak-btn" onclick="checkSpeaking(1, 'a')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; color: #333; text-align: left;">
                                A) Îro Duşem e.
                            </button>
                            <button class="speak-btn" onclick="checkSpeaking(1, 'b')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; color: #333; text-align: left;">
                                B) Sibe Duşem e.
                            </button>
                        </div>
                        <div id="speak-feedback-1" style="margin-top: 15px; font-weight: bold;"></div>
                    </div>

                    <div style="margin: 25px 0; padding: 20px; background: #fff9c4; border-radius: 10px;">
                        <h4 style="color: #f57f17; margin-bottom: 15px;">Scenario 2: Someone asks "Sibe tu çi dikî?"</h4>
                        <p style="margin-bottom: 10px;"><strong>What do you say?</strong></p>
                        <div style="display: flex; flex-direction: column; gap: 10px;">
                            <button class="speak-btn" onclick="checkSpeaking(2, 'a')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; color: #333; text-align: left;">
                                A) Duh ez çûm dibistanê.
                            </button>
                            <button class="speak-btn" onclick="checkSpeaking(2, 'b')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; color: #333; text-align: left;">
                                B) Sibe ez diçim dibistanê.
                            </button>
                        </div>
                        <div id="speak-feedback-2" style="margin-top: 15px; font-weight: bold;"></div>
                    </div>

                    <div id="speak-score" style="margin-top: 25px; font-size: 1.3rem; font-weight: bold; text-align: center;">
                        Score: <span id="speak-correct">0</span> / 2
                    </div>
                </div>
            </div>

            <!-- Section 7: Culture - Newroz -->
            <div class="section">
                <h2 class="section-title"><span class="section-icon">🌿</span>7. Çand (Culture): Newroz - Kurdish New Year</h2>
                <p style="font-size: 1.1rem; margin-bottom: 20px;">Learn about Newroz, the most important Kurdish celebration:</p>
                
                <div style="background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 30px; border-radius: 15px; margin: 20px 0; border: 3px solid #fbc02d;">
                    <h3 style="color: #f57f17; text-align: center; margin-bottom: 25px;">🔥 Newroz - 21 Adar</h3>
                    
                    <div style="background: white; padding: 20px; margin: 15px 0; border-radius: 10px; border-left: 4px solid #f9a825;">
                        <h4 style="color: #f57f17; margin-bottom: 10px;">🔥 What is Newroz?</h4>
                        <p style="line-height: 1.8;">
                            <strong>Newroz</strong> is the Kurdish New Year, celebrated on <strong>March 21</strong>. It marks the beginning of spring and symbolizes renewal, freedom, and resistance. For Kurds, Newroz is the most important celebration of the year.
                        </p>
                    </div>

                    <div style="background: white; padding: 20px; margin: 15px 0; border-radius: 10px; border-left: 4px solid #f9a825;">
                        <h4 style="color: #f57f17; margin-bottom: 10px;">📖 The Legend of Kawa</h4>
                        <p style="line-height: 1.8;">
                            The story tells of <strong>Kawa the Blacksmith</strong> who defeated the tyrant king Dehak. Kawa lit a fire on the mountain to signal victory. This fire became the symbol of Newroz - the victory of light over darkness.
                        </p>
                    </div>

                    <div style="background: white; padding: 20px; margin: 15px 0; border-radius: 10px; border-left: 4px solid #f9a825;">
                        <h4 style="color: #f57f17; margin-bottom: 10px;">🎉 How Kurds Celebrate</h4>
                        <p style="line-height: 1.8;">
                            • <strong>Lighting fires (Agir)</strong> - Bonfires symbolizing Kawa's fire<br>
                            • <strong>Dancing (Govend)</strong> - Traditional Kurdish circle dances<br>
                            • <strong>Wearing traditional clothes</strong><br>
                            • <strong>Picnics in nature</strong><br>
                            • <strong>Special foods and music</strong>
                        </p>
                    </div>

                    <div style="background: white; padding: 20px; margin: 15px 0; border-radius: 10px; border-left: 4px solid #f9a825;">
                        <h4 style="color: #f57f17; margin-bottom: 10px;">💡 Newroz Greeting</h4>
                        <p style="line-height: 1.8; font-size: 1.2rem; color: #f57f17; font-weight: bold;">
                            Newroza we pîroz be! 🔥<br>
                            <span style="font-size: 1rem; color: #666; font-weight: normal; font-style: italic;">(Happy Newroz!)</span>
                        </p>
                    </div>
                </div>
            </div>

            <!-- Section 8: Review -->
            <div class="section">
                <h2 class="section-title"><span class="section-icon">🔤</span>8. Dubare (Review): Vocabulary Practice</h2>
                
                <div class="exercise-box">
                    <div class="exercise-title">🎯 Exercise A: Match Days</div>
                    <p style="margin-bottom: 20px; color: #666;">Match the Kurdish days with English:</p>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 20px 0;">
                        <div>
                            <h4 style="color: #f9a825; margin-bottom: 15px;">Kurdish Days</h4>
                            <div style="display: flex; flex-direction: column; gap: 10px;">
                                <button class="match-btn-c10" data-word="duşem" onclick="selectWordC10('duşem')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• Duşem</button>
                                <button class="match-btn-c10" data-word="çarşem" onclick="selectWordC10('çarşem')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• Çarşem</button>
                                <button class="match-btn-c10" data-word="în" onclick="selectWordC10('în')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• În</button>
                                <button class="match-btn-c10" data-word="yekşem" onclick="selectWordC10('yekşem')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• Yekşem</button>
                            </div>
                        </div>
                        <div>
                            <h4 style="color: #f57f17; margin-bottom: 15px;">English</h4>
                            <div style="display: flex; flex-direction: column; gap: 10px;">
                                <button class="match-trans-c10" data-trans="monday" onclick="selectTransC10('monday')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• Monday</button>
                                <button class="match-trans-c10" data-trans="wednesday" onclick="selectTransC10('wednesday')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• Wednesday</button>
                                <button class="match-trans-c10" data-trans="friday" onclick="selectTransC10('friday')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• Friday</button>
                                <button class="match-trans-c10" data-trans="sunday" onclick="selectTransC10('sunday')" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; text-align: left; color: #333;">• Sunday</button>
                            </div>
                        </div>
                    </div>
                    <div style="text-align: center; margin: 20px 0;">
                        <button onclick="resetVocabC10()" style="background: #ff9800; padding: 10px 20px; border: none; border-radius: 8px; color: white; cursor: pointer;">🔄 Reset</button>
                    </div>
                    <div id="vocab-match-feedback" style="margin-top: 20px; font-size: 1.2rem; font-weight: bold; text-align: center;"></div>
                </div>

                <div class="exercise-box" style="margin-top: 30px;">
                    <div class="exercise-title">🎯 Exercise B: Important Dates</div>
                    <p style="margin-bottom: 20px; color: #666;">Complete with the correct month:</p>
                    
                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">1. Newroz 21 ___ e. (Newroz is March 21)</label>
                        <input type="text" id="month-q1" placeholder="Type the month...">
                        <div id="month-q1-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <div style="margin: 15px 0;">
                        <label style="font-weight: bold; display: block; margin-bottom: 8px;">2. Roja Zimanê Kurdî 15 ___ e. (Kurdish Language Day is August 15)</label>
                        <input type="text" id="month-q2" placeholder="Type the month...">
                        <div id="month-q2-feedback" style="margin-top: 8px; font-weight: bold;"></div>
                    </div>

                    <button onclick="checkMonths()">✓ Check Answers</button>
                    <div id="month-score" style="margin-top: 15px; font-size: 1.2rem; font-weight: bold;"></div>
                </div>
            </div>

            <div class="section" style="text-align: center; background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);">
                <h2 style="color: #f57f17; margin-bottom: 20px;">🎉 Pîroz be! Congratulations!</h2>
                <p style="font-size: 1.2rem; margin-bottom: 20px;">You've completed Course 10: Time & Days!<br>You can now talk about dates and time in Kurdish.</p>
                <a href="../level-a1.html" class="back-link" style="background: #f9a825;">← Back to Course Selection</a>
            </div>
        </div>
    </main>
    <footer><p>&copy; 2025 Kurdish Academy. All rights reserved.</p></footer>
    <script>
        function checkTimeWords() {
            let correct = 0;
            const total = 3;
            
            const q1 = document.getElementById('time-q1').value.toLowerCase().trim();
            const q1Feedback = document.getElementById('time-q1-feedback');
            if (q1.includes('îro') || q1.includes('iro')) {
                correct++;
                q1Feedback.innerHTML = '✅ Correct! Îro Duşem e.';
                q1Feedback.style.color = '#2e7d32';
            } else {
                q1Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>îro</strong>';
                q1Feedback.style.color = '#d32f2f';
            }
            
            const q2 = document.getElementById('time-q2').value.toLowerCase().trim();
            const q2Feedback = document.getElementById('time-q2-feedback');
            if (q2.includes('sibe')) {
                correct++;
                q2Feedback.innerHTML = '✅ Correct! Sibe ez diçim malê.';
                q2Feedback.style.color = '#2e7d32';
            } else {
                q2Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>sibe</strong>';
                q2Feedback.style.color = '#d32f2f';
            }
            
            const q3 = document.getElementById('time-q3').value.toLowerCase().trim();
            const q3Feedback = document.getElementById('time-q3-feedback');
            if (q3.includes('duh')) {
                correct++;
                q3Feedback.innerHTML = '✅ Correct! Duh em li parkan bûn.';
                q3Feedback.style.color = '#2e7d32';
            } else {
                q3Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>duh</strong>';
                q3Feedback.style.color = '#d32f2f';
            }
            
            const scoreDiv = document.getElementById('time-score');
            scoreDiv.textContent = `Score: ${correct} / ${total}`;
            scoreDiv.style.color = correct === total ? '#2e7d32' : '#f57f17';
        }

        function checkListening() {
            let correct = 0;
            const total = 2;
            
            const q1 = document.getElementById('listen-q1').value.toLowerCase().trim();
            const q1Feedback = document.getElementById('listen-q1-feedback');
            if (q1.includes('duşem') || q1.includes('dusem') || q1.includes('monday')) {
                correct++;
                q1Feedback.innerHTML = '✅ Correct! Duşem.';
                q1Feedback.style.color = '#2e7d32';
            } else {
                q1Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>Duşem</strong>';
                q1Feedback.style.color = '#d32f2f';
            }
            
            const q2 = document.getElementById('listen-q2').value.toLowerCase().trim();
            const q2Feedback = document.getElementById('listen-q2-feedback');
            if (q2.includes('15') && (q2.includes('gulan') || q2.includes('may'))) {
                correct++;
                q2Feedback.innerHTML = '✅ Correct! 15 Gulan.';
                q2Feedback.style.color = '#2e7d32';
            } else {
                q2Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>15 Gulan</strong>';
                q2Feedback.style.color = '#d32f2f';
            }
            
            const scoreDiv = document.getElementById('listen-score');
            scoreDiv.textContent = `Score: ${correct} / ${total}`;
            scoreDiv.style.color = correct === total ? '#2e7d32' : '#f57f17';
        }

        function checkReading() {
            let correct = 0;
            const total = 2;
            
            const q1 = document.getElementById('read-q1').value.toLowerCase().trim();
            const q1Feedback = document.getElementById('read-q1-feedback');
            if (q1.includes('21') && (q1.includes('adar') || q1.includes('march'))) {
                correct++;
                q1Feedback.innerHTML = '✅ Correct! 21 Adar.';
                q1Feedback.style.color = '#2e7d32';
            } else {
                q1Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>21 Adar</strong>';
                q1Feedback.style.color = '#d32f2f';
            }
            
            const q2 = document.getElementById('read-q2').value.toLowerCase().trim();
            const q2Feedback = document.getElementById('read-q2-feedback');
            if (q2.includes('cejn') || q2.includes('bihar') || q2.includes('spring') || q2.includes('festival') || q2.includes('newroz')) {
                correct++;
                q2Feedback.innerHTML = '✅ Correct! Cejna biharê.';
                q2Feedback.style.color = '#2e7d32';
            } else {
                q2Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>Cejna biharê</strong>';
                q2Feedback.style.color = '#d32f2f';
            }
            
            const scoreDiv = document.getElementById('read-score');
            scoreDiv.textContent = `Score: ${correct} / ${total}`;
            scoreDiv.style.color = correct === total ? '#2e7d32' : '#f57f17';
        }

        function checkWriting() {
            const schedule = document.getElementById('write-schedule').value.trim();
            const feedback = document.getElementById('write-feedback');
            if (schedule.length < 30) {
                feedback.innerHTML = '❌ Please write at least 4-5 sentences.';
                feedback.style.color = '#d32f2f';
            } else {
                feedback.innerHTML = '✅ Great! Your schedule has been submitted.';
                feedback.style.color = '#2e7d32';
            }
        }

        let speakCorrect = 0;
        function checkSpeaking(scenario, answer) {
            const feedback = document.getElementById(`speak-feedback-${scenario}`);
            if (scenario === 1 && answer === 'a') {
                speakCorrect++;
                feedback.innerHTML = '✅ Correct! Îro Duşem e.';
                feedback.style.color = '#2e7d32';
            } else if (scenario === 2 && answer === 'b') {
                speakCorrect++;
                feedback.innerHTML = '✅ Correct! Sibe ez diçim dibistanê.';
                feedback.style.color = '#2e7d32';
            } else {
                feedback.innerHTML = '❌ Try again.';
                feedback.style.color = '#d32f2f';
            }
            document.getElementById('speak-correct').textContent = speakCorrect;
        }

        const vocabPairs = {
            'duşem': 'monday',
            'çarşem': 'wednesday',
            'în': 'friday',
            'yekşem': 'sunday'
        };
        let selectedWord = null;
        let selectedTrans = null;
        let matchedPairs = 0;

        function selectWordC10(word) {
            if (document.querySelector(`[data-word="${word}"]`).classList.contains('matched')) return;
            document.querySelectorAll('.match-btn-c10').forEach(btn => btn.style.background = 'white');
            document.querySelector(`[data-word="${word}"]`).style.background = '#fff9c4';
            selectedWord = word;
            checkMatch();
        }

        function selectTransC10(trans) {
            if (document.querySelector(`[data-trans="${trans}"]`).classList.contains('matched')) return;
            document.querySelectorAll('.match-trans-c10').forEach(btn => btn.style.background = 'white');
            document.querySelector(`[data-trans="${trans}"]`).style.background = '#fff9c4';
            selectedTrans = trans;
            checkMatch();
        }

        function checkMatch() {
            if (selectedWord && selectedTrans) {
                if (vocabPairs[selectedWord] === selectedTrans) {
                    document.querySelector(`[data-word="${selectedWord}"]`).style.background = '#c8e6c9';
                    document.querySelector(`[data-trans="${selectedTrans}"]`).style.background = '#c8e6c9';
                    document.querySelector(`[data-word="${selectedWord}"]`).classList.add('matched');
                    document.querySelector(`[data-trans="${selectedTrans}"]`).classList.add('matched');
                    matchedPairs++;
                    if (matchedPairs === 4) {
                        document.getElementById('vocab-match-feedback').innerHTML = '🎉 Perfect!';
                        document.getElementById('vocab-match-feedback').style.color = '#2e7d32';
                    }
                } else {
                    document.querySelector(`[data-word="${selectedWord}"]`).style.background = '#ffcdd2';
                    document.querySelector(`[data-trans="${selectedTrans}"]`).style.background = '#ffcdd2';
                    setTimeout(() => {
                        document.querySelector(`[data-word="${selectedWord}"]`).style.background = 'white';
                        document.querySelector(`[data-trans="${selectedTrans}"]`).style.background = 'white';
                    }, 1000);
                }
                selectedWord = null;
                selectedTrans = null;
            }
        }

        function resetVocabC10() {
            document.querySelectorAll('.match-btn-c10, .match-trans-c10').forEach(btn => {
                btn.style.background = 'white';
                btn.classList.remove('matched');
            });
            selectedWord = null;
            selectedTrans = null;
            matchedPairs = 0;
            document.getElementById('vocab-match-feedback').innerHTML = '';
        }

        function checkMonths() {
            let correct = 0;
            const total = 2;
            
            const q1 = document.getElementById('month-q1').value.toLowerCase().trim();
            const q1Feedback = document.getElementById('month-q1-feedback');
            if (q1.includes('adar') || q1.includes('march')) {
                correct++;
                q1Feedback.innerHTML = '✅ Correct! Adar (March).';
                q1Feedback.style.color = '#2e7d32';
            } else {
                q1Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>Adar</strong>';
                q1Feedback.style.color = '#d32f2f';
            }
            
            const q2 = document.getElementById('month-q2').value.toLowerCase().trim();
            const q2Feedback = document.getElementById('month-q2-feedback');
            if (q2.includes('tebax') || q2.includes('august')) {
                correct++;
                q2Feedback.innerHTML = '✅ Correct! Tebax (August).';
                q2Feedback.style.color = '#2e7d32';
            } else {
                q2Feedback.innerHTML = '❌ Wrong. Correct answer: <strong>Tebax</strong>';
                q2Feedback.style.color = '#d32f2f';
            }
            
            const scoreDiv = document.getElementById('month-score');
            scoreDiv.textContent = `Score: ${correct} / ${total}`;
            scoreDiv.style.color = correct === total ? '#2e7d32' : '#f57f17';
        }
    </script>
</body>
</html>'''
    
    # Write the complete file
    with open('course-10.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Course 10 created successfully!')
else:
    print('Error: Could not find Section 1 end marker')
