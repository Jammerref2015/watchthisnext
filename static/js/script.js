$(document).ready(function(){
  $('.sidenav').sidenav();
  $('select').formSelect();
  $('.datepicker').datepicker({
      format: "yyyy",
      yearRange: 30,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
  })
})