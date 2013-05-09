$(document).ready(function() {
    console.log(event.which);
    $('body').keypress(function(event) {
        console.log(event.which);
        if (event.which === 119)
        {
            $('#result').load('/forward');
        }
        else if (event.which === 115)
        {
            $('#result').load('/reverse');
        }
        else if (event.which === 97)
        {
            $('#result').load('/left');
        }
        else if (event.which === 100)
        {
            $('#result').load('/right');
        }
    });
});


