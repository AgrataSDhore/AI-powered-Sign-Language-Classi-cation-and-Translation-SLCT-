function validate(){

    //Ckecking it there any empty values
    if(document.login.idTb.value==""){
        alert("Please provide your user id !");
        document.login.idTb.focus();
        return false;
    }

}