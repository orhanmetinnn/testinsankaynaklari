$(document).ready(function () {
    $('#newsletterForm').on('submit', function (event) {
        event.preventDefault(); // Sayfanın yenilenmesini engelle
        $.ajax({
            url: '',  // Formun gönderileceği URL
            type: 'post',
            data: $(this).serialize(),
            success: function (data) {
                if (data.success) {
                    $('#successMessage').show(); // Başarı mesajını göster
                    $('#mailregisterinput').val(''); // Formu temizle
                    window.history.pushState(null, null, window.location.href); // Geçici URL güncelleme
                } else {
                    var errorMessage = 'Bir hata oluştu: ';
                    if (data.errors.email) {
                        errorMessage += data.errors.email[0];
                    }
                    alert(errorMessage); // Hata mesajını göster
                }
            },
            error: function (data) {
                alert('Bir hata oluştu, lütfen tekrar deneyin.');
            }
        });
    });
});
