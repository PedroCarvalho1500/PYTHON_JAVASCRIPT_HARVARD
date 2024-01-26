function manipulate1(){
    const h1_element = document.querySelector("h1");
    console.log(h1_element);
    if (h1_element.innerHTML == "Hello, World!"){
        //console.log("ENTERED")
        h1_element.innerHTML = 'Goodbye'
    }
    else{
        h1_element.innerHTML = 'Hello, World!'
    }
    //document.querySelector('h1').innerText = 'Goodbye'
    
}