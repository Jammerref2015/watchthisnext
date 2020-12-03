$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.modal').modal();
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