var langs_voices = {'en': {'lang': 'English', 'voices': ['Microsoft David Desktop - English (United States)', 'Microsoft Zira Desktop - English (United States)', 'Google UK English Male', 'Google UK English Female']},
	'ru': {'lang': 'Russian', 'voices': ['Google русский']},
	'nl': {'lang': 'Dutch', 'voices': ['Google Nederlands']},
	'de': {'lang': 'German', 'voices': ['Google Deutsch']},
	'fr': {'lang': 'French', 'voices': ['Google français']},
	'es': {'lang': 'Spanish', 'voices': ['Google español', 'Google español de Estados Unidos']},
	'pl': {'lang': 'Polish', 'voices': ['Google polski']},
	'lt': {'lang': 'Lithuanian', 'voices': ['Chrome Lietuvių']},
	'el': {'lang': 'Greek', 'voices': ['Google Ελληνικά']},
	'hi': {'lang': 'Hindi', 'voices': ['Google हिन्दी']},
}

$(function() {

	$('onLoad', function() {

		displayBrowserSupportMsg()
		loadAvailableVoices()
		controls(false, true, true, true)
		statistics()

		$('select[name="languages"]').change(function(){
			language = $(this).val()
			loadFilteredVoices(langs_voices[language]['voices'])
		});  // radio buttons lang

		$('#play').click(function(){
			controls(true, false, true, false)
			read()
		});  // click Play

		$('#pause').click(function(){
			controls(true, true, false, true)
			window.speechSynthesis.pause()
		});  // click Pause

		$('#resume').click(function(){
			controls(true, false, true, false)
			window.speechSynthesis.resume()
		});  // click Resume

		$('#stop').click(function(){
			controls(false, true, true, true)
			window.speechSynthesis.cancel()
		});  // click Stop

		$('#categories').change(function(){
			pid = $('#categories').val();
			selectSubcategories = document.getElementById('subcategories')
			$.getJSON('/_get_subcategories/' + pid, {}, function(data) {
				selectSubcategories.innerHTML = '' 
				for (i=0; i<data.length; i++) {
					option = document.createElement('option')
					option.value = data[i][0];
					option.innerHTML = data[i][2];
					selectSubcategories.append(option);
				}
			});  // getJSON
		});  // change categories - load subcategories

		$('input[name="lang_checkbox"]').on('change', function(e) {
			if ($('input[name="lang_checkbox"]:checked').length > 5) {
				this.checked = false;
				alert('Max 5 languages allowed')
			}
		});  // $('input[name="lang_checkbox"]').on

		$('#stories').on('change', function(e){
			$.post('/_get_story/', {'longtext': $('#stories').val()}, function(data) {
				$('#longtext').html(data)
			});  // post
		});  // $('#stories').on


		$('table').on('click', 'i[name="del_row"]', function(e){
			$(this).closest('tr').remove()
		});  // $('table').on

		$('table').on('click', 'i[name="say_word"]', function(e){
			$('#stop').click()
			item = $(this).closest('td')
			word = item.text()
			lang = item.attr('id').substring(0, 2)
			say(word, lang)
		}); //$('table').on

		$('#add_to_db').on('click', function(e){
			translations = {}
			$('td[id$="_value"]').each(function() {
				translations[this.id.substring(0, 2)] = $(this).html()
			});
			$.post('/_add_to_db/', {'translations': JSON.stringify(translations), 'subcategory': document.getElementById('subcategory').value}, function(data) {
				data = JSON.parse(data)
				content = '' 
				for (i=0; i<data.length; i++) {
					content += '<div class="alert alert-'+data[i][0]+' alert-dismissible" role="alert" width="100%">'
					content += '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>'
					content += '<strong>' + data[i][0][0].toUpperCase() + data[i][0].slice(1) + '!</strong> ' + data[i][1]
					content += '</div>'
				}
				$('#flashes').html(content)
			});  // post
		});  // $('#add_to_db').on

		return false;
	});  // onLoad function()

});  // function()


function statistics() {
	$.getJSON('/_get_statistics/', {}, function(data) {
		msg = 'Statistics: the database contains ' + data['words'] + ' unique English words/phrases '
		msg += 'translated into ' + (data['languages'] - 1) + ' other languages '
		msg += 'and classified into ' + data['subcategories'] + ' subcategories '
		msg += 'within ' + data['categories'] + ' categories as ' + data['relations'] + ' links.'
		$('#statistics').html(msg)
	});  // getJSON
}


function controls(play_off, pause_off, resume_off, stop_off) {
	$('#play').attr('disabled', play_off)
	$('#pause').attr('disabled', pause_off)
	$('#resume').attr('disabled', resume_off)
	$('#stop').attr('disabled', stop_off)
} // function controls


function read() {
	text = $('#longtext')
	if (!!text.val()) {
		text = text.val().replace('!', '.').replace('?', '.')
		sentences = text.split('.')
		for (i = 0; i < sentences.length; i++) {
			sentence = sentences[i]
			speak(sentence)
		}
	} else {
		$('i[name="say_word"]').each(function(e) {
			item = $(this).closest('td')
			word = item.text()
			lang = item.attr('id').substring(0, 2)
			say(word, lang)
		})
	}
} // function read()


function speak(message) {
	volumeInput = document.getElementById('volume');
	rateInput = document.getElementById('rate');
	pitchInput = document.getElementById('pitch');
	msg = new SpeechSynthesisUtterance();
	msg.text = message;
	msg.volume = parseFloat(volumeInput.value);
	msg.rate = parseFloat(rateInput.value);
	msg.pitch = parseFloat(pitchInput.value);
	selectVoice = document.getElementById('voice')
	if (selectVoice.value) {
		msg.voice = speechSynthesis.getVoices().filter(function(voice) {
			return voice.name == selectVoice.value; 
		})[0];
	}
	window.speechSynthesis.speak(msg);
} // function speak(message)


function say(word, lang) {
	volumeInput = document.getElementById('volume');
	rateInput = document.getElementById('rate');
	pitchInput = document.getElementById('pitch');
	msg = new SpeechSynthesisUtterance();
	msg.text = word;
	msg.volume = parseFloat(volumeInput.value);
	msg.rate = parseFloat(rateInput.value);
	msg.pitch = parseFloat(pitchInput.value);
	lang_voice = langs_voices[lang]['voices'][0]
	msg.voice = speechSynthesis.getVoices().filter(function(voice) {
		return voice.name == lang_voice;
	})[0];
	for (i=0; i<document.getElementById('repeat').value; i++) {
		window.speechSynthesis.speak(msg);
	}
} // function say(word, lang)


function loadAvailableVoices() {
	//by default load Voices for English only
	loadFilteredVoices(langs_voices['en']['voices']);
	// Chrome loads voices asynchronously.
	window.speechSynthesis.onvoiceschanged = function(e) {
		loadFilteredVoices(langs_voices['en']['voices'])
	};
} // function loadAvailableVoices()


function loadFilteredVoices(expectedVoices) {
	var availableVoices = speechSynthesis.getVoices();
	filteredVoices = []
	for (i=0; i<availableVoices.length; i++) {
		if (expectedVoices.indexOf(availableVoices[i].name) > -1) {
			filteredVoices.push(availableVoices[i])
		}
	}
	selectVoice = $('#voice')
	selectVoice.empty() 
	filteredVoices.forEach(function(voice, i) {
		option = document.createElement('option')
		option.value = voice.name;
		option.innerHTML = voice.name;
		selectVoice.append(option);
	});
} // function loadFilteredVoices(expectedVoices)


function displayBrowserSupportMsg() {
	supportMsg = document.getElementById('msg')
	if ('speechSynthesis' in window) {
		supportMsg.innerHTML = 'Your browser <strong>supports</strong> speech synthesis.'
	} else {
		supportMsg.innerHTML = 'Your browser <strong>does not support</strong> speech synthesis.'
		supportMsg.classList.add('not-supported')
	}
} // function displayBrowserSupportMsg()
       
