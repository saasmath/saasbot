$(document).ready(function() {

    $('body').keydown(function(event) {
        console.log(event.which);
        if (event.which === 87) //w
        {
            $('#result').load('/webbytes?bytes=145,0,50,0,50');
            event.preventDefault();
        }
        else if (event.which === 83) //s
        {
            $('#result').load('/webbytes?bytes=145,255,206,255,206');
            event.preventDefault();

        }
        else if (event.which === 65) //a
        {
            $('#result').load('/webbytes?bytes=145,0,50,255,206');
            event.preventDefault();

        }
        else if (event.which === 68) //d
        {
            $('#result').load('/webbytes?bytes=145,255,206,0,50');
            event.preventDefault();

        }
        else if (event.which === 32) //space bar
        {
            $('#result').load('/webbytes?bytes=145,0,0,0,0');
            event.preventDefault();
        }
        else if (event.which === 66) //b
        {
            $('#result').load('/brake');
            event.preventDefault();
        }
        else if (event.which === 38) //up arrow
        {
            $('#result').load('/accelerate');
            event.preventDefault();
        }
        else if (event.which === 40) //down arrow
        {
            $('#result').load('/decelerate');
            event.preventDefault();
        }
        else if (event.which === 37) //left arrow
        {
            $('#result').load('/goleft');
            event.preventDefault();
        }
        else if (event.which === 39) //right arrow
        {
            $('#result').load('/goright');
            event.preventDefault();
        }
    });

});

