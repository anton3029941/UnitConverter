function convert(type){
    let fromunit = document.getElementById("from_").value;
    let tounit = document.getElementById("to_").value;
    let converto = document.getElementById("value_").value;
    
    fetch(`http://127.0.0.1:5000/convert?fromun=${fromunit}&toun=${tounit}&value=${converto}&type=${type}`)
        .then(response => response.json())
        .then(data => {document.getElementById("result").innerText = data.result})
        .catch(error => console.error(error));
}