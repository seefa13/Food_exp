// *********************************************************************
// How to write instructions:
// - myQuestions : list element [] containing all questions as JSON objects
// - Each question requires the following fields:
//     1. question: String containing the question itself
//     2. name: string with the input name for this question
//     3. type: Type of question (+ shows additional fields required):
//          - radio: multiple choice question. Options are presented vertically
//              + values (default: likertValues):    list with the value to be input for each possible answer (stored data)
//              + labels (default: likertScale):    list. In case you want to label the possible answers, 
//                                     you need to provide a list with one label per value
//          - radioH: multiple choice question. Options are presented horizontally
//              + values (default: likertValues):    list with the value to be input for each possible answer (stored data)
//              + labels (default: likertScale):    list. In case you want to label the possible answers, 
//                                     you need to provide a list with one label per value
//          - scale: bar scale (similar to radioH) with buttons instead of radio buttons
//              + values (default: likertValues):    list with the value to be input for each possible answer (stored data)
//              + limits (default: likertLimits):    list with the left and right extreme labels
//          - autocomplete: Text input with list to autocomplete
//              + list: list with possible options to autocomplete 
//          - shortOpen: Text input (one row to write)
//              + validate: function with str input. Returns true if answer is valid.
//              + invalidMessage: str explaining why form is invalid
//          - longOpen: Text input for long Text. (5 rows to write) 
//              + validate: function with str input. Returns true if answer is valid.
//              + invalidMessage: str explaining why form is invalid
// *********************************************************************

// *********************************************************************
// Add here any lists that you require for the questions
// Add here any validation function
// *********************************************************************
function validInt(str) {return (!isNaN(parseInt(str)))};
function validAge(str) {
    num = parseInt(str);
    return (num>=18 && num<= 122);
};
function labels() {
    var indexL = indexl;
    var label = Labellist.at(indexL);
    indexl = indexl + 1;
    return label;
};
function tasteQ() {
    var indexQ = indexF;
    var Fooditem = Foodlist.at(indexQ);
    var Fooditem_b = Foodlist.at(indexQ).bold();
    indexF = indexF + 1;
    if (Fooditem == 'Water' || Fooditem == 'Milk' || Fooditem == 'a Soja-Drink' || Fooditem == 'Lemonade' || Fooditem == 'a Berrysmoothie (vegan)') {
        var Q = "On a scale from 1 to 5, how much would you like to drink "+Fooditem_b+". Remember that, 1s will be excluded.";
    } else {
        var Q = "On a scale from 1 to 5, how much would you like to eat "+Fooditem_b+". Remember that, 1s will be excluded.";   
    };
    return Q;
};

const likertScale = [ 'Would never like to eat', 'Would most likely not like to eat', 'Neutral', 'Would most likely not like to eat', 'Would definitely like to eat'];
const likertValues = [1,2,3,4,5];
const warningAutocomplete = 'Please select one item from the list';
const warningEmpty = 'Please do not leave this question unanswered';
const likertLimits = ['Would never like to eat','Would definitely like to eat'];
const Foodlist = [
    'a Banana',             'Strawberries',         'Chia seeds',       'Chips',                    'Salmon',
    'a Vegetable mix',      'White Beans',          'Yogurt',           'Whole Grain Bread (vegan)','a Chickenfilet',
    'Chocolate (vegan)',    'a Croissant (vegan)',  'Pork',             'a sugarfree Mueslibar',    'Water',
    'Cheese (vegan)',       'a Boiled Egg',         'Banana chips',     'a Berrysmoothie (vegan)',  'Vanilla Ice Cream (vegan)',
    'salted Cashews',       'smoked Salmon',        'Hummus',           'sweetened Cranberries',    'sweetened Yogurt (Soja)',
    'White Bread (vegan)',  'a breaded Chicken filet','Butter (vegan)', 'Milk',                     'a Sausage (Pork)',        
    'a sweetened Mueslibar','Lemonade',             'Cheese',           'Crackers',                 'a Soja-Drink',
    'Ravioli Funghi',       'salted Popcorn'
];
const Labellist = [
    'iFruit',               'iBerries',             'iSeeds',           'iChips',                   'iFish', 
    'iVeg',                 'iBeans',               'iYog',             'iBread',                   'iChicken', 
    'iChoco',               'iCroissant',           'iRedmeat',         'iBar',                     'iDrink', 
    'iCheese_h',            'iEggs',                'iFruit_unh',       'iBerries_unh',             'iIce', 
    'iNuts_unh',            'iFish_unh',            'iHummus',          'iCran',                    'iYog_unh', 
    'iBread_unh',           'iChicken_unh',         'iButter_unh',      'iMilk',                    'iRedmeat_unh', 
    'iBar_unh',             'iDrink_unh',           'iCheese_unh',      'iCracker',                 'iSoja', 
    'iRavioli',             'iPopcorn',             'V1',               'V2'
];
var indexl = 0;
var indexF = 0;
// bold text
introtxt1 = "honestly and candidly as you can";
introtxt1_b = introtxt1.bold();
introtxt2 = "incentive to state your true preference for a food product";
introtxt2_b = introtxt2.bold();
introtxt3 = "excluded from the experiment";
introtxt3_b = introtxt3.bold();


// *********************************************************************
// Add Your Questions here
// *********************************************************************

const firstQuestions = [
    {
        question: "For the following questions, please answer each of these questions in terms of the way you generally feel. For each question simply state as "+introtxt1_b+" what you are presently experiencing. Note that you have an "+introtxt2_b+", since you will not see the names of the food products in later decisions. Please Select '2' to show that you read these instructions.",
        name: "V1",
        type: "scale",
    },
    {
        question: "Taste ratings do not influence your monetary payments. You can rate food items from 1 (I would never like eat that due to moral, allergy or taste reasons) to 5 (I would definitely like to eat that). Food items with the rating 1 will be "+introtxt3_b+". Please note that we have to exclude you from the experiment if you rate too many items with 1. Please select '3' to show that you read these instructions.",
        name: "V3",
        type: "scale",
    },
];

// Add questionnaire questions in different orders
const shuffleQuestions = [ 
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: tasteQ(),
        name: labels(),
        type: "scale",
    },
    {
        question: "To show you are paying attention, please select '1'.",
        name: "V2",
        type: "scale",
    },     
];
  

// *********************************************************************
// YOU DO NOT NEED TO MODIFY ANYTHING BELOW THIS POINT. 
// *********************************************************************

// Dynamic variables
var slideIndex = 0;
// Constants and Scales
const myQuestions = firstQuestions.concat(shuffleArray(shuffleQuestions));
const maxQ  = myQuestions.length;
const height = 70;
const width = 80;

const BackButtonProps = [
    {
        sName: 'type',
        sProperty: 'button',
    },
    {
        sName: 'class',
        sProperty: 'button QT-Back',
    },
    {
        sName: 'onclick',
        sProperty: `backSlide()`,
    },
];

const FinalButtonProps = [
    {
        sName: 'class',
        sProperty: 'button QT-Next',
    },
];



// Initialize
document.addEventListener("DOMContentLoaded", function() {

    // Create Slides
    let divAnswers = document.getElementById('final-answers');
    let counter = 0;
    myQuestions.forEach(question => { 
        // Create slide
        let slide = new QuestionSlide(counter,question);
        counter++;
        slide.printSlide();
        // Create input
        let input   = document.createElement('input');
        input.type  = 'hidden';
        input.value = '';
        input.name  = question.name;
        input.id    = question.name;
        divAnswers.appendChild(input);
        // Add autocomplete if necessary
        if (question.type==='autocomplete') {
                autocomplete(document.getElementById(`answer-${question.name}`), question.list);
        }
    });
    // prevent submitting the questionnaire if user click "Enter"
    $(document).ready(function () {
        $(window).keydown(function (event) {
            if (event.keyCode == 13) {
                event.preventDefault();
                return false;
            }
        });
    });

    // Show first slide
    showSlides(slideIndex);
});

// Define Class: QuestionSlides
function QuestionSlide(iNumber, jsonQuestion) {
        this.iSlideNumber = iNumber;
        this.Question = jsonQuestion;
};

QuestionSlide.prototype.printSlide = function() {
    // Create Slide
    let slideQuestion = document.createElement('div');
    slideQuestion.className = 'question-slide fade';
    slideQuestion.id = `slide-${this.Question.name}`;
    // Create Question
    let pQuestion = document.createElement('p');
    pQuestion.className = 'question';
    pQuestion.innerHTML = this.Question.question;
    slideQuestion.appendChild(pQuestion);
    // Create Image
    function img_create(src) {
        var img = document.createElement('img');
        img.src = src;
        slideQuestion.appendChild(img);
    }
    // Depending on input type, create inputs accordingly
    if (this.Question.type==='radio' || this.Question.type==='radioH' || this.Question.type==='radioFig') {
        // 1. Radio or RadioHorizontal
        let div = writeRadio(this.Question);
        slideQuestion.appendChild(div);
    } else if ( this.Question.type==='scale' ) {
        let div = writeScale(this.Question);
        slideQuestion.appendChild(div);
    } else if (this.Question.type==='longOpen') {
        // Div container for input and Next Button
        let div     = document.createElement('div');
        div.className = 'div-input-text';
        // Create input
        let input   = document.createElement('textarea');
        input.rows  = '5';
        input.type  = 'text';
        input.className = 'input-text';
        input.name  = `answer-${this.Question.name}`;
        input.id    = `answer-${this.Question.name}`;
        input.cols  = '50';
        // Create next button
        let NextButton = writeNextButton(this.Question.name);
        // Nest elements and append them to html
        div.appendChild(input);
        div.innerHTML += NextButton;
        slideQuestion.appendChild(div);
        // Create warning message
        if (typeof this.Question.validate==='function') {
            let errorMessage = document.createElement('div');
            errorMessage.className = 'error-message fade';
            errorMessage.id = `warning-${this.Question.name}`;
            errorMessage.style.visibility = 'hidden';
            if (typeof this.Question.invalidMessage==='string') {
                errorMessage.innerHTML = invalidMessage;
            } else {
                errorMessage.innerHTML = 'Please enter a valid answer'
            }    
            slideQuestion.appendChild(errorMessage);
        }    
    
    } else if ( this.Question.type==='shortOpen' || this.Question.type==='autocomplete') {
        // Div container for input and Next Button
        let div     = document.createElement('div');
        div.className = 'div-input-text';
        // Create input
        let input   = document.createElement('input');
        input.type  = 'text';
        input.name  = `answer-${this.Question.name}`;
        input.id    = `answer-${this.Question.name}`;
        input.className = 'input-text';
        input.rows = '1';
        input.cols  = '50';
        input.placeholder = 'Type here...'
        // Add autocomplete
        if (this.Question.type ==='autocomplete') {
            input.className = 'autocomplete';
        }
        // Create wrapping form
        let form   = document.createElement('form');
        form.autocomplete  = 'off';
        form.action  = '/action_page.php';
        // Create next button
        let NextButton = writeNextButton(this.Question.name);
        // Nest elements and append them to html
        form.appendChild(input);
        div.appendChild(form);
        div.innerHTML += NextButton;
        slideQuestion.appendChild(div);
        // Create warning message
        if (typeof this.Question.validate==='function') {
            let errorMessage = document.createElement('div');
            errorMessage.className = 'error-message fade';
            errorMessage.id = `warning-${this.Question.name}`;
            errorMessage.style.visibility = 'hidden';
            if (typeof this.Question.invalidMessage==='string') {
                errorMessage.innerHTML = this.Question.invalidMessage;
            } else {
                errorMessage.innerHTML = 'Please enter a valid answer'
            }
            slideQuestion.appendChild(errorMessage);
        } else if (this.Question.type ==='autocomplete') {
            let errorMessage = document.createElement('div');
            errorMessage.className = 'error-message fade';
            errorMessage.id = `warning-${this.Question.name}`;
            errorMessage.style.visibility = 'hidden';
            errorMessage.innerHTML = warningAutocomplete;
            slideQuestion.appendChild(errorMessage);
        }
    } else if (this.Question.type==='final') {
        let ContinueButton = writeTag('button','Continue',FinalButtonProps);
        slideQuestion.innerHTML += ContinueButton;
    }

    // Create back button

    let BackButton = writeTag('button','Back',BackButtonProps);
    // let BackButton = `<button type="button" class="button QT-Back" onclick="backSlide()" > Back </button>`
    // Create progress bar
    let progBar = writeProgBar(this.iSlideNumber)
    // Add Button and ProgressBar
    if (this.iSlideNumber>0) {slideQuestion.innerHTML+=BackButton};
    slideQuestion.innerHTML+= progBar;
    container = document.getElementsByClassName('element-container')[0];
    container.appendChild(slideQuestion);

};
// *********************************************************************
// Function Name:   writeRadio(Question)
// Functionality:
//                  1. writes the labels contianing radio inputs
//                  2. Joins all inputs in one div
//
// input:           sQuestion, string with the question name
//                  
// returns:         string with the html line
// ********************************************************************
function writeRadio(Question) {
    // Create div for inputs
    let div = document.createElement('div');
    div.className = `div-input-${Question.type}`;
    // Check if values and labels are predetermined
    let values = [];
    let labels = [];
    if (typeof Question.values === 'undefined' || Question.values === null) {
        values =likertValues;
        labels =likertScale 
    } else {
        values = Question.values
        // Check if labels for the values exist
        if (typeof Question.labels === 'undefined' || Question.labels === null) {
            labels = Question.values; 
        } else {
            labels = Question.labels;
        }
    }
    // Check that labels and values have the same length
    if (labels.length != values.length) {
        console.log(`Question ${Question.name}: Dimensions of labels and values do not match`)
    };
    // Write inputs within div
    for (let i=0; i<values.length; i++) {
        // create input (for some reason I could not add the onclick command via js, so I input this as html)
        let input = "";
        if (Question.type==='radio') {
            input = `<label class="QT-${Question.type}"> 
            <input type="radio" class="answer-${Question.name}" id="answer-${Question.name}-${i}" onclick="nextSlide('${Question.name}', '${values[i]}')"> 
            ${labels[i]} </label>`;
        } else if (Question.type==='radioH') {
            input = `<label class="QT-${Question.type}">  ${labels[i]}
            <input type="radio" class="answer-${Question.name}" id="answer-${Question.name}-${i}" onclick="nextSlide('${Question.name}', '${values[i]}')"> 
                </label>`;
        } else if (Question.type==='radioFig') {
            input = `<button type="button" class="img-button" onclick="nextSlide('${Question.name}', '${values[i]}')"> 
                    <img class="mini-graph" src="${labels[i]}"> </button>` ;
        }
        div.innerHTML +=input;
    }

    return div; 
}

// *********************************************************************
// Function Name:   writeScale(Question)
// Functionality:
//                  1. the html code for a Scale question
//                  2. puts all necessary elements within a div
//
// input:           Question: Question object from myQuestions
//                  
// returns:         div with necessary elements
// ********************************************************************
function writeScale(Question) {
    // Check if values and limits are predetermined
    let values = [];
    let limits = [];
    if (typeof Question.values === 'undefined' || Question.values === null) {
        values =likertValues;
        limits =likertLimits; 
    } else {
        values = Question.values
        limits = Question.limits; 
    };
    // Create input container
    let div = document.createElement('div');
    div.className = `div-input div-input-${Question.type}`;
    // Add Left extreme of scale
    div.innerHTML = `<label class="limit_left"> ${limits[0]} </label> `;
    
    // Add Buttons
    for (i=0;i<values.length;i++) {
        let lProps = [
            {
                sName: 'class',
                sProperty: 'ScaleButton',
            },
            {
                sName: 'type',
                sProperty: 'button',
            },
            {
                sName: 'onclick',
                sProperty: `nextSlide('${Question.name}',sValue='${values[i]}')`
            }
        ];
        div.innerHTML += writeTag('button',values[i],lProps);
    };
    div.innerHTML +=  ` <label class="limit_right"> ${limits[1]} </label>`;
    return div;
}

// *********************************************************************
// Function Name:   writeNextButton('sQuestion')
// Functionality:
//                  1. writes a Tag for the Next button, and adds the functions specific to sQuestions' name
//
// input:           sQuestion, string with the question name
//                  
// returns:         string with the html line
// ********************************************************************
function writeNextButton(sQuestion) {
    let NextButtonProps = [
        {
            sName: 'type',
            sProperty: 'button',
        },
        {
            sName: 'class',
            sProperty: 'button QT-Next',
        },
        {
            sName: 'onclick',
            sProperty: `nextSlide('${sQuestion}')`,
        },
    ];

    return writeTag('button','Next',NextButtonProps);
}


// *********************************************************************
// Function Name:   writeProgBar()
// Functionality:
//                  1. writes a Tag with the specified requirements
//
// input:           sTag: Tag for the input (default: div)
//                  sInnerHTML: content inside (default: "")
//                  lAttr : list of object with all attributes. 
//                      - sName: string with the name of the attribute
//                      - sProperty: string with properties
//                  
// returns:         string with the html line
// ********************************************************************
function writeProgBar(slide) {
    return `<div class="pbar-container"> <label> 0% </label>
    <progress class="progress-bar" min="0" max="${maxQ}" value="${slide+1}"></progress>
                        <label> 100% </label> </div>`
}

function writeImg(src) {
    return `<img class="img-food" src="{% static ${src} %}" width="150px" height="35px" />`
}

// *********************************************************************
// Function Name:   writeTag()
// Functionality:
//                  1. writes a Tag with the specified requirements
//
// input:           sTag: Tag for the input (default: div)
//                  sInnerHTML: content inside (default: "")
//                  lAttr : list of object with all attributes. 
//                      - sName: string with the name of the attribute
//                      - sProperty: string with properties
//                  
// returns:         string with the html line
// ********************************************************************
function writeTag(sTag,sInnerHTML,lAttr) {
    str = `<${sTag}`;
    lAttr.forEach(elem => {
        str += ` ${elem.sName}="${elem.sProperty}"`;
    }); 
    str += `> ${sInnerHTML} </${sTag}>`;
    return str;
}

// *********************************************************************
// Function Name:   backSlide
// Functionality:
//                  1. Checks if question is answered, clears it
//                  2. Goes to the previous slide
//
// input:           null
// returns:         void
// ********************************************************************

function backSlide() {
    // uncheck answer current question
    checkAnswer(true);
    // go to previous slide
    plusSlides(-1);
    // uncheck answer previous question
    checkAnswer(true);

}



// *********************************************************************
// Function Name:   nextSlide
// Functionality:
//                  1. Checks if question is answered
//                      and adds it to the inputs
//                  2. Goes to next slide
//
// input:           sQuestionName : name of the question
//                  sValue: (default="")
// returns:         void
// ********************************************************************

function nextSlide(sQuestionName,sValue="") {
   
    if (checkAnswer()) {
        let input = document.getElementById(sQuestionName);
        if (sValue==="") {
            // Retrieve answer from forms
            let answer = document.getElementById(`answer-${sQuestionName}`).value;
            input.value =  answer;
        } else {
            input.value = sValue;
        }
    // go to next slide
    plusSlides(1);
    } else {
        let warning = document.getElementById(`warning-${sQuestionName}`);
        warning.style.visibility = 'visible';
    }

}


// *********************************************************************
// Function Name:   checkAnswer
// Functionality:
//                  1. Checks if question is answered
//                  2. In case it's needed, cleans it
//
// input:           iSlideNumber:   slide number from myQuestions
//                  bClean:         Boolean, empties answer if true
// returns:         true, if questions has been answered
//                  false, if question is empty
// ********************************************************************

function checkAnswer(bClean=false) {
    let Question = myQuestions[slideIndex];
    let qType = Question.type;
    if (qType==='radio' || qType==='radioH' ) {
        let inputs = document.getElementsByClassName(`answer-${Question.name}`);
        if (bClean) { 
            console.log(`Question ${Question.name} cleared`);
            for (let i = 0; i<Question.values.length; i++) {
                inputs[i].checked = false;
            }
            return false
        } else {
            let bAnswered = false;
            for (let i = 0; i<Question.values.length; i++) {
                if (inputs[i].checked == true) {bAnswered=true}
            }
            return bAnswered;
        };
    } else if (qType === 'longOpen'|| qType === 'shortOpen'|| qType === 'autocomplete') {
        // clean input if needed
        let input = document.getElementById(`answer-${Question.name}`);
        if (bClean) {
            console.log(`Question ${Question.name} cleaned`);
            input.value = ""
        }
        // Check if question needs to be validated:
        if (qType==='autocomplete') {
            return Question.list.includes(input.value);
        } else if (typeof Question.validate==="function" ) {
            // if required function
            return Question.validate(input.value);
        } else {
            // if no requirement, return true
            return true;
        }
    } else if (qType === 'scale' || qType === 'radioFig') {return true}; // These inputs have nothing to be cleared
}

// *********************************************************************
// Function Name:   plusSlides
// Functionality:   
//                  1. Changes slide index by adding n
//                  2. Shows slide SlideIndex+n 
//
// Source: https://www.w3schools.com/howto/howto_js_slideshow.asp
//
// input:           n: Number of slides to be skipped
//
// returns:         void
// *********************************************************************

// Advance a slide
function plusSlides(n) {
  showSlides(slideIndex += n);
}
// *********************************************************************
// Function Name:   currentSlide
// Functionality:   
//                  1. Changes slide index to n
//                  2. Shows slide n 
//
// Source: https://www.w3schools.com/howto/howto_js_slideshow.asp
//
// input:           n: Number of slides to be skipped
//
// returns:         void
// *********************************************************************


// Show current slide
function currentSlide(n) {
  showSlides(slideIndex = n);
}

// *********************************************************************
// Function Name:   showSlides
// Functionality:   Display current slide, hide the rest
// Source: https://www.w3schools.com/howto/howto_js_slideshow.asp
//
// input:           n: Slide number to be shown
// returns:         void
// ********************************************************************
function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("question-slide");
    // Go back when reaching the end
    if (n >= slides.length) {
        document.getElementById('final-button').click();
    } 
    // Avoid negative slide counter
    if (n < 1) {0};
  
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex].style.display = "flex";  
  
  }
// *********************************************************************
// Function Name:   autocomplete
// Functionality:   Create autocomplete for text inputs
// Source: https://www.w3schools.com/howto/howto_js_autocomplete.asp
// input:           inp: HTML object, input that needs autocomplete
//                  arr: array of autocomplete options
// returns:         void
// ********************************************************************

  function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function (e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false; }
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
            /*check if the item starts with the same letters as the text field value:*/
            if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
                /*create a DIV element for each matching element:*/
                b = document.createElement("DIV");
                /*make the matching letters bold:*/
                b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
                b.innerHTML += arr[i].substr(val.length);
                /*insert a input field that will hold the current array item's value:*/
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function (e) {
                    /*insert the value for the autocomplete text field:*/
                    inp.value = this.getElementsByTagName("input")[0].value;
                    /*close the list of autocompleted values,
                    (or any other open lists of autocompleted values:*/
                    closeAllLists();
                });
                a.appendChild(b);
            }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function (e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            /*If the arrow DOWN key is pressed,
            increase the currentFocus variable:*/
            currentFocus++;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 38) { //up
            /*If the arrow UP key is pressed,
            decrease the currentFocus variable:*/
            currentFocus--;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 13) {
            /*If the ENTER key is pressed, prevent the form from being submitted,*/
            e.preventDefault();
            if (currentFocus > -1) {
                /*and simulate a click on the "active" item:*/
                if (x) x[currentFocus].click();
            }
        }
    });
    function addActive(x) {
        /*a function to classify an item as "active":*/
        if (!x) return false;
        /*start by removing the "active" class on all items:*/
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        /*add class "autocomplete-active":*/
        x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
        /*a function to remove the "active" class from all autocomplete items:*/
        for (var i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt) {
        /*close all autocomplete lists in the document,
        except the one passed as an argument:*/
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    /*execute a function when someone clicks in the document:*/
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
}

// *********************************************************************
// Function Name:   shuffleArray()
// Functionality:   shuffles an array 
// Source: https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
// input:           array
// returns:         array, shuffled
// ********************************************************************


function shuffleArray(array) {
    var currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
  
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
  }