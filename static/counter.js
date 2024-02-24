

const ans_btn = document.querySelectorAll('.ans_btn');
const answer = document.getElementById('answer').getAttribute('name');
let score = document.getElementById('score');
console.log(score);
let score_placeholder = parseInt(document.getElementById('score').getAttribute('placeholder'))
console.log(score_placeholder)

ans_btn.forEach(btn => {
    btn.addEventListener('click', (e)=>{

        show_answer = document.getElementById('show_answer')
        if (parseInt(e.target.innerHTML) == answer) {
            console.log("correct answer");
            show_answer.setAttribute('style', "color:blue;")
            show_answer.innerHTML = "Correct";
            score_placeholder += 1;
        } else {
            console.log("wrong answer");
            console.log(parseInt(e.target.innerHTML));
            show_answer.setAttribute('style', "color:red;")
            show_answer.innerHTML = "Wrong";
            score_placeholder -= 1;
        }
        score.value = String(score_placeholder)
        document.getElementById('score').setAttribute("placeholder", String(score_placeholder))
        //call a submit form after 2 seconds
        setTimeout(() => {
            
            document.getElementById("submit_selections").requestSubmit();
          }, 2000);
        

    });
});