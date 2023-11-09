$('.show').click(function(){
    $(this).toggleClass('fa-eye-slash');
    var prev = $(this).prev();
    if ('password' == prev.attr('type')) {
      prev.prop('type', 'text');
    } else {
     prev.prop('type', 'password');
    }
});