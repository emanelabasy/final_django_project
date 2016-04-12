 window.onload=function()
    {
        var fpass=false;

        var passspan=document.getElementById("spass");
        // var conftxt=document.registration.elements["repassword"];
        var passtxt=document.getElementById("password");
        var conftxt=document.getElementById("repassword");  
        function checkall()
        {
            return(fpass);
        }
        conftxt.onblur=function()
        {
            if(passtxt.value.length>=6&&conftxt.value.length==passtxt.value.length)
            {
                fpass=false;
                passtxt.className="";
                conftxt.className="";
                passspan.style.display="none";
            }
            else
            {
                fpass=true;
                passtxt.className="Error";
                conftxt.className="Error";
                passtxt.focus();
                //passtxt.select;
                // conftxt.focus();
                passspan.style.display="block";
            }
        }
    }