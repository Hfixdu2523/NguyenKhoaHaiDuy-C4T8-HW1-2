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
var answer = {
    a: 0,
    b: 0,
    c: 0,
}
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
    if (question.length === 0) {
        return
    } else {
        var renderHTML = `
        <div id="${item.id}">
            <div>${item.id}</div>
            <div>${item.question}</div>
            <div>Answer</div>
            <ul>
                <div><button class="btn" id='btn1'><li>${item.answer.a}</li></button></div>
                <div><button class="btn" id='btn2'><li>${item.answer.b}</li></button></div>
                <div><button class="btn" id='btn3'><li>${item.answer.c}</li></button></div>
            </ul>
        </div>
        `;
        DOMquestions.insertAdjacentHTML("beforeend", renderHTML);
        // Loai bo thang item khoi List
        question = RemoveItemChoice(question, item)
    }
}

function check(answer) {
    if (answer.a + answer.b + answer.c <= 9) {
        return true
    } else {
        console.log("Het cau hoi");
        return false
    }
}

//Ham handle button
function score() {
    var button = document.getElementById('btn1');
    button.onclick = function() {
        if (check(answer)) {
            answer.a += 1;
            console.log("Answer A:" + answer.a);
        }
        // console.log("CLick bnt1");
    };

    var button2 = document.getElementById('btn2');
    button2.onclick = function() {
        if (check(answer)) {
            answer.b += 1;
            console.log("Answer B:" + answer.b);
        }
    };

    var button3 = document.getElementById('btn3');
    button3.onclick = function() {
        if (check(answer)) {
            answer.c += 1;
            console.log("Answer C:" + answer.c);
        }
    };
}

//Goi Ham Tren
showQuestion();
score();
var final;
function judge(){
    var pending = {           
        most_a: 'You are high',
        most_b: 'You are not high',
        most_c: 'You are normal',
        other:'You are oofted',            
    };
        

        
        
    if (answer.a > answer.b && answer.a > answer.c){
        final = pending.most_a;
    } else if (answer.b > answer.a && answer.b > answer.c){
        final = pending.most_b;
    } else if (answer.c > answer.b && answer.c > answer.a){
        final = pending.most_c;
    } else {
        final = pending.other;
    }
};

// var something = document.getElementsByClassName('other');
// something.addEventListener('click', function(){
    
// });

// Ham nay de gan cac su kien vao nut click
var ListButton = document.getElementsByClassName("btn");
function loop(){   
    
    
    for (var j = 0; j < ListButton.length; j++) {
        if (question.length === 0) {
            //Xu ly sau khi het cau hoi
            DOMquestions.innerHTML = "";
            console.log(answer);
            var render = `
            <div>${final}</div>
            `;
            DOMquestions.insertAdjacentHTML("afterbegin", render);
        } else {
            ListButton[j].addEventListener("click", function() {
                DOMquestions.innerHTML = ""
                showQuestion();
                loop();
                score();
                judge();
            });
        }
    }
}

loop();







