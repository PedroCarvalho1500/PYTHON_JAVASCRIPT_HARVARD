if (!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}
function count(){
    //alert('Hello, world!')
    let counter = localStorage.getItem('counter');
    counter++;
    console.log(counter);
    //alert(counter);
    //myTitle = document.getElementById("click_here").innerHTML;
    //console.log(myTitle);
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter',counter);

    if (counter % 10 === 0){
        alert(`Count is now ${counter}`)
    }

    //WAIT UNTIL ALL OF THE CONTENT HAS LOADED BEFORE ASSIGNING THE FUNCTION TO THE BUTTON

}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');   
    document.querySelector("button.count_button").onclick = count;
    //setInterval(count, 1000);
                //document.querySelector("button.count_button").addEventListener('click', count);
    })