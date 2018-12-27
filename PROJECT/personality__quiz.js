// Data
var question = [
    {
        id:1,
        question:'What would you do after a badly done exam?',
        answer:{
            a: 'A. Weep in tears',
            b: 'B. Forget immediately',
            c: 'C. Act tough but dead inside',
        }
    },
    {
        id:2,
        question: "How would you react to beaing bullied?",
        answer: {
            a: 'A. Keep quiet and suffer',
            b: 'B. Ask for help from friends and family to deal with the situation',
            c: 'C. Report teachers and keep away from the bullies',
        }
    },
    {
        id:3,
        question: "When you see your crush walking with another boy/girl?",
        answer: {
            a: 'A. Remain quiet accept fate',
            b: 'B. Make a move and confess',
            c: 'C. Pray that they are just friends',
        }
    },
    {
        id:4,
        question: "Failing at school and/or in life?",
        answer: {
            a: 'A. Regret your existence',
            b: 'B. I am not failing but rather school and/or life is failing me',
            c: 'C. Act like usual but inside, you are more sensitive than ever',
        }
    },
    {
        id:5,
        question: "If you are in an intense quarrel with a close friend?",
        answer: {
            a: 'A. Feel regretful but probably let everything slide and never talk again. FOREVER',
            b: 'B. Apologise and rebuild your friendship',
            c: 'C. Pacify but stick his/her name on your black book',
        }
    },
    {
        id:6,
        question: "Find out that your money has been stolen?",
        answer: {
            a: 'A. Weep in tears',
            b: 'B. Forget immediately',
            c: 'C. Act tough but dead inside',
        }
    },
    {
        id:7,
        question: "You see another student being gang-bullied. What would you do?",
        answer: {
            a: 'A. Weep in tears',
            b: 'B. Forget immediately',
            c: 'C. Act tough but dead inside',
        }
    },
    {
        id:8,
        question: "Your favorite book series has just been cancelled. How do you respond?",
        answer: {
            a: 'A. Weep in tears',
            b: 'B. Forget immediately',
            c: 'C. Act tough but dead inside',
        }
    },
    {
        id:9,
        question: "You get a chance to walk home alone with your crush. You:",
        answer: {
            a: 'A. Weep in tears',
            b: 'B. Forget immediately',
            c: 'C. Act tough but dead inside',
        }
    },
    {
        id:10,
        question: "You see a box of puppies left on the pavement. What do you do?",
        answer: {
            a: 'A. Weep in tears',
            b: 'B. Forget immediately',
            c: 'C. Act tough but dead inside',
        }
    }
];

// Function - Excute
function RemoveItemChoice(list, item) {
    var quesList = list.filter(function(element){
        return element.id !== item.id
    });
    return quesList;
}   

var DOMquestions = document.getElementById("questions");

function showQuestion() {
    // Chon random 1 thang trong cau hoi
    var item = question[Math.floor(Math.random()*question.length)];
    // Render ra HTML
    var renderHTML = `
    <div id="${item.id}">
        <div>${item.id}</div>
        <div>${item.question}</div>
        <div>Answer</div>
        <ul>
            <div><button class="btn"><li>${item.answer.a}</li></button></div>
            <div><button class="btn"><li>${item.answer.b}</li></button></div>
            <div><button class="btn"><li>${item.answer.c}</li></button></div>
        </ul>
    </div>
    `;
    DOMquestions.insertAdjacentHTML("beforeend", renderHTML);
    // Loai bo thang item khoi List
    
    question = RemoveItemChoice(question, item)
}
//Goi Ham Tren
showQuestion();

var ListButton = document.getElementsByClassName("btn");
// Ham nay de gan cac su kien vao nut click
function loop(){
    for (var j = 0; j < ListButton.length; j++) {
        ListButton[j].addEventListener("click", function() {
            DOMquestions.innerHTML = ""
            showQuestion();
            loop();
        });
    }
}

loop();


