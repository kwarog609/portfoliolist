
console.log("pwede")

const ans_btn = document.querySelectorAll('.ans_btn');
const answer_tag = document.getElementById('answer');
console.log(answer_tag)
const answer = (answer_tag.getAttribute('name'));

ans_btn.forEach(btn => {

    btn.addEventListener('click', (e)=>{

        console.log("clicked");

        console.log(answer)
        if (parseInt(e.target.innerHTML) == answer) {
            console.log("correct answer");
            alert("Correct Answer");
        } else {
            console.log("wrong answer");
            console.log(parseInt(e.target.innerHTML));
        }

    });
});