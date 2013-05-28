$(document).ready(function() {

    $('body').keydown(function(event) {
        console.log(event.which);

        if (event.which === 87)
        {
            $('#result').load('/webbytes?bytes=145,0,50,0,50');
        }
        else if (event.which === 83)
        {
            //    $('#result').load('/reverse');
            $('#result').load('/webbytes?bytes=145,255,206,255,206');
        }
        else if (event.which === 65)
        {
            $('#result').load('/webbytes?bytes=145,0,50,255,206');
        }
        else if (event.which === 68)
        {
            $('#result').load('/webbytes?bytes=145,255,206,0,50');
        }
        else if (event.which === 32)
        {
            $('#result').load('/webbytes?bytes=145,0,0,0,0');
        }

        else if (event.which === 38)
        {
            $('#result').load('/accelerate');
        }
        else if (event.which === 40)
        {
            $('#result').load('/decelerate');
        }
        else if (event.which === 37)
        {
            $('#result').load('/goleft');
        }
        else if (event.which === 39)
        {
            $('#result').load('/goright');
        }
    });

});

