((win,doc)=> {
    'use strict';

 if(doc.querySelector('.btnDel')) {
     let btnDel  = doc.querySelectorAll('.btnDel');

     for(let i=0; i < btnDel.length; i++){
         btnDel[i].addEventListener('click',(e)=>{
            if(confirm('Deseja apagar realmente este cliente?')) {
                return true;

            }else {
                e.preventDefault()
            }
         })
     }
 }
})(window,document)