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

// by setting readonly to false 'required' on the html element works
$(".datepicker").prop('readonly', false);

$( function() {
    $('#jump_to').change(function(){
       $('#date_form').submit();
    });
 });


// gets the recipe id to the modal
$('.modal').modal({
  ready: function(modal, trigger) {
      modal.find('input[name="recipe_id"]').val(trigger.data('id'))
  }
});

$('select').material_select();
document.querySelectorAll('.select-wrapper').forEach(t => t.addEventListener('click', e=>e.stopPropagation()))

