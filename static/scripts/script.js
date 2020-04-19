$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: true, // Close upon selecting a date,
    container: undefined, // ex. 'body' will append picker to body
    format: 'yyyy-mm-dd'
  });

$('.datepicker').on('mousedown',function(event){
    event.preventDefault();
})

$( function() {
    $('#jump_to').change(function(){
       $('#date_form').submit();
    });
 });