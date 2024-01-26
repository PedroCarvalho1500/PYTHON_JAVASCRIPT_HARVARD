let counter = 0;
function count(){
    //alert('Hello, world!')
    counter++;
    console.log(counter);
    //alert(counter);
    //myTitle = document.getElementById("click_here").innerHTML;
    //console.log(myTitle);
    document.querySelector('h1').innerHTML = counter;
    
    if (counter % 10 === 0){
        alert(`Count is now ${counter}`)
    }

    //WAIT UNTIL ALL OF THE CONTENT HAS LOADED BEFORE ASSIGNING THE FUNCTION TO THE BUTTON

}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("button.count_button").onclick = count;
                //document.querySelector("button.count_button").addEventListener('click', count);
    })