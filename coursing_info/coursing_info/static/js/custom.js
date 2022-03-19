$(document).ready(function() {
    $('#example').dataTable( {
        "oLanguage": {
        "sSearch":"جستجو:",
        "sShow ":"نمایش",
        "sEntries":"",
        "sInfo":"",
        "oPaginate": {
        "sFirst": "صفحه اول", // This is the link to the first page
        "sPrevious": "قبلی", // This is the link to the previous page
        "sNext": "بعدی", // This is the link to the next page
        "sLast": "صفحه آخر" // This is the link to the last page
        }
        }
        } );


      



          var pathname = window.location.pathname;
          pathname = pathname.replace('/', '');
          $('.'+pathname).addClass('nav-item-active')



          $('.mobile_menu').click(function(){
            if($('aside').hasClass('menu-open')==true){
              $('aside').removeClass('menu-open')
              $('aside').addClass('menu-close')
              $('main').css('width','100%')
            }
            else{
              $('aside').removeClass('menu-close')
              $('aside').addClass('menu-open')
              $('main').css('width','75%')

            }
          })



          if ($(window).width() <= 480) {
            $('aside').addClass('menu-close')
            $('main').css('width','100%')

          }

} );