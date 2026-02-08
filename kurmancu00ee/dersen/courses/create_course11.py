content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course 11 - Rojane (Daily Routine) | Kurdish Academy</title>
    <link rel="stylesheet" href="../../../styles.css">
    <link rel="stylesheet" href="../../../chatbot.css">
    <script src="../../../scripts.js"></script>
    <script src="../../../chatbot-ai.js"></script>
    <style>
        .course-page { max-width: 1200px; margin: 0 auto; padding: 40px 20px; }
        .course-header { text-align: center; margin-bottom: 50px; padding: 30px; background: linear-gradient(135deg, #f9a825 0%, #fdd835 100%); border-radius: 20px; color: white; }
        .course-header h1 { font-size: 2.5rem; margin-bottom: 10px; }
        .course-header .course-meta { font-size: 1.1rem; opacity: 0.95; }
        .back-link { display: inline-block; margin-bottom: 20px; padding: 10px 20px; background: #2e7d32; color: white; text-decoration: none; border-radius: 20px; transition: all 0.3s ease; }
        .back-link:hover { background: #1b5e20; transform: translateX(-5px); }
        .section { background: white; padding: 30px; margin-bottom: 30px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
        .section-title { font-size: 2rem; color: #2e7d32; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
        .section-icon { font-size: 2.5rem; }
        .vocab-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }
        .vocab-card { background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 20px; border-radius: 12px; text-align: center; transition: transform 0.3s ease, box-shadow 0.3s ease; border: 2px solid #fbc02d; }
        .vocab-card:hover { transform: translateY(-5px); box-shadow: 0 6px 12px rgba(249, 168, 37, 0.2); }
        .vocab-word { font-size: 1.4rem; font-weight: bold; color: #f57f17; margin-bottom: 8px; }
        .vocab-translation { font-size: 1rem; color: #f9a825; }
        .structure-box { background: #fffde7; padding: 25px; border-radius: 12px; margin: 20px 0; border-left: 5px solid #fbc02d; }
        .structure-pattern { font-size: 1.2rem; color: #f57f17; margin: 15px 0; padding: 15px; background: white; border-radius: 8px; }
        .example-dialogue { background: #fff9c4; padding: 20px; border-radius: 12px; margin: 20px 0; }
        .dialogue-line { margin: 15px 0; padding: 15px; background: white; border-radius: 8px; }
        .speaker { font-weight: bold; color: #f9a825; margin-bottom: 8px; }
        .kurdish-text { font-size: 1.2rem; color: #333; margin: 8px 0; }
        .translation { font-size: 0.95rem; color: #666; font-style: italic; }
        .exercise-box { background: #f9fbe7; padding: 25px; border-radius: 12px; margin: 20px 0; border: 2px solid #cddc39; }
        .exercise-title { font-size: 1.5rem; color: #827717; margin-bottom: 15px; font-weight: bold; }
        .exercise-box input[type="text"], .exercise-box textarea { width: 100%; padding: 12px; margin: 10px 0; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; }
        .exercise-box button { background: #fbc02d; color: white; padding: 12px 30px; border: none; border-radius: 8px; font-size: 1.1rem; cursor: pointer; transition: all 0.3s ease; }
        .exercise-box button:hover { background: #f9a825; transform: scale(1.05); }
    </style>
</head>
<body>
    <nav>
        <div class="logo">Kurdish Academy</div>
        <ul>
            <li><a href="../../../index.html">Serrûpel (Home)</a></li>
            <li><a href="../../dersen.html">Ders (Lessons)</a></li>
            <li><a href="../../peyv/peyv.html">Peyv (Vocabulary)</a></li>
            <li><a href="../../leker/leker.html">Lêker (Verbs)</a></li>
            <li><a href="../../reziman/reziman.html">Rêziman (Grammar)</a></li>
            <li><a href="../../guhdarikirn/guhdarikirn.html">Guhdarîkirin (Listening)</a></li>
            <li><a href="../../xwendin/xwendin.html">Xwendin (Reading)</a></li>
            <li><a href="../../nivisandin/nivisandin.html">Nivîsandin (Writing)</a></li>
            <li><a href="../../axaftin/axaftin.html">Axaftin (Speaking)</a></li>
        </ul>
    </nav>
    <main class="course-page">
        <a href="../level-a1.html" class="back-link">← Back to A1 Courses</a>
        <div class="course-header">
            <h1>⏰ Course 11: Rojane</h1>
            <div class="course-meta">Daily Routine | A1 Level</div>
        </div>
        <div class="course-content">
'''

with open('course-11.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Course 11 header created")
