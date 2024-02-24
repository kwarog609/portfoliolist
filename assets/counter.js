

//const ans_btn = document.querySelectorAll('.ans_btn');
const ans_btn = document.getElementsByName('ans_btn')
const answer = document.getElementById('answer').getAttribute('name');
let score = document.getElementById('score');
console.log("th initial value is " + score.value);
let score_placeholder = document.getElementById('score')

if (isNaN(score.value)){
    score.value = 0
}


ans_btn.forEach(btn => {
    btn.addEventListener('click', (e)=>{

        show_answer = document.getElementById('show_answer')
        if (parseInt(e.target.innerHTML) == answer) {
            console.log("correct answer");
            show_answer.setAttribute('style', "color:blue;")
            show_answer.innerHTML = "Correct";
            score_placeholder.setAttribute('placeholder', 'correct');
            score.value = parseInt(score.value) + 1;
        } else {
            console.log("wrong answer");
            console.log(parseInt(e.target.innerHTML));
            show_answer.setAttribute('style', "color:red;")
            show_answer.innerHTML = "Wrong";
            score_placeholder.setAttribute('placeholder', 'wrong');
            score.value = parseInt(score.value) -1;
        }

        console.log("the set attribute is: " + score_placeholder.getAttribute('placeholder'));
        console.log("the set score is: " + score.value)

        
        //call a submit form after 2 seconds

        setTimeout(() => {
            
            document.getElementById("submit_selections").requestSubmit();
          }, 2000);
        

    });
});