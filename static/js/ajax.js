/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/*
Property                        Description
--------------------------------------------------------------------------------------------
onreadystatechange	Stores a function (or the name of a function) to be called automatically each time the readyState property changes
----------------------------------------------------------------------------------------------------------------
readyState              Holds the status of the XMLHttpRequest. Changes from 0 to 4: 
                        0: request not initialized 
                        1: server connection established
                        2: request received 
                        3: processing request 
                        4: request finished and response is ready
--------------------------------------------------------------------------------------------
status                  200: "OK"
                        404: Page not found
*/
var ajaxErrorText,ajaxErrorStatus;
/*var errorWin=false;
function ajaxError(status,responseText)
{
    if(!errorWin)
    {
        errorWin = window.open('', '_blank');
        errorWin.document.open();
    }
    errorWin.document.write("");
    errorWin.document.write(responseText);
    errorWin.onbeforeunload = function() {
        errorWin=false;
    }
}*/
function getBack(url,handler)
{
    var xmlhttp = "";
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
       xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4)
        {
            if(xmlhttp.status==200)
                handler(xmlhttp.responseText);
            else
            {
                ajaxErrorText=xmlhttp.responseText;
                ajaxErrorStatus=xmlhttp.status;
            } 
        }
    }
    xmlhttp.open("GET",url,true);
    xmlhttp.send(); 
}
function postBack(url,params,handler)
{
    /*$.ajax({
        url: url,
        data: params,
        error:handler,
        success: handler,
        type: 'POST'
     }); */
    var xmlhttp = "";
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4)
        {
            if(xmlhttp.status==200)
                handler(xmlhttp.responseText);
            else
            {
                console.error(xmlhttp.responseText);
                ajaxErrorText=xmlhttp.responseText;
                ajaxErrorStatus=xmlhttp.status;
            }
        }
    }
    xmlhttp.open("POST",url,true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    //xmlhttp.setRequestHeader("Content-length", params.length);
    //xmlhttp.setRequestHeader("Connection", "close");
    xmlhttp.send(params);  
}

function syncPostBack(url,params,handler)
{
    var xmlhttp = "";
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4)
        {
            if(xmlhttp.status==200)
                handler(xmlhttp.responseText);
            else
            {
                ajaxErrorText=xmlhttp.responseText;
                ajaxErrorStatus=xmlhttp.status;
            }
        }
    }
    xmlhttp.open("POST",url,false);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader("Content-length", params.length);
    xmlhttp.setRequestHeader("Connection", "close");
    xmlhttp.send(params);  
}
