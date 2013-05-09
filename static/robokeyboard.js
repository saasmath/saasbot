$(document).ready(function() {
    console.log(event.which);
    $('body').keypress(function(event) {
        console.log(event.which);
        if (event.which === 119)
        {
        //    $('#result').load('/forward');
        //    $('#result').load('/webbytes?bytes=137,0,8,128,0');
            $('#result').load('/webbytes?bytes=137,1,144,128,0');
        }
        else if (event.which === 115)
        {
        //    $('#result').load('/reverse');
        $('#result').load('/webbytes?bytes=137,255,0,128,0');
        }
        else if (event.which === 97)
        {
            $('#result').load('/left');
        }
        else if (event.which === 100)
        {
            $('#result').load('/right');
        }
        else if (event.which === 32)
        {
            $('#result').load('/webbytes?bytes=137,0,0,128,0');
        }
    });
});


