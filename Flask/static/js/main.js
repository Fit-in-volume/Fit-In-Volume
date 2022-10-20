$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-calculate').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });
    
    $('#btn-calculate1').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        var str_html = '';
        var html_btn = '<button type="button" class="btn btn-success m-1" id="btn" style="width:100px"></button>';
        str_html = str_html + html_btn + '\n';
        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/calculate1',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result1').fadeIn(600);
                $('#result1').text(data);
                $('#div_btn').html(str_html);
                console.log('Success!');
            },
        });
    });
    $('#btn-calculate2').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        var str_html = '';
        var html_btn = '<button type="button" class="btn btn-success m-1" id="btn" style="width:100px"></button>';
        str_html = str_html + html_btn + '\n';
        // Show loading animation
        $(this).hide();
        $('.loader').show();    
        $.ajax({
            type: 'POST',
            url: '/calculate2',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result2').fadeIn(600);
                $('#result2').text(data);
                $('#div_btn').html(str_html);
                console.log('Success!');
            },
        });
    });

});
