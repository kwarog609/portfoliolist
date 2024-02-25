
console.log("entered js");
//const ans_btn = document.querySelectorAll('.ans_btn');
const ans_btn = document.getElementsByName('ans_btn');

console.log(ans_btn);
ans_btn.forEach(btn => {
    console.log("entred loop")
    btn.addEventListener('click', (e)=>{
        console.log("event binded");

        //read_question = String(document.getElementById('question').innerHTML);
        //speechSynthesis.speak(new SpeechSynthesisUtterance(read_question));

    });

});


