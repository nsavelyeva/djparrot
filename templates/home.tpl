% include('_header.tpl', title='DJ Parrot - Home')
<div class="container">
	<div class="row">
		<div class="col-9">
			% include('_nav_bar.tpl')
			<div>
				<textarea id="longtext" style="visibility:hidden">
					Hi! My name is DJ Parrot! I am a small web application to help you learn foreign languages.
				</textarea>

				<h5>Meet DJ Parrot!</h5>
				<p>
				DJ Parrot is a very small web application which can (or cannot) help you to learn foreign languages
				by listening and repeating words aloud, just like parrots do :-)
				The application keeps all the words in the database on the remote server,
				and speech synthesis happens locally on the client (your browser).
				</p>

				<h5>Usage:</h5>
				<p>
					<ul>
						<li>Just launch run.py and open <a href="http://127.0.0.1">http://127.0.0.1</a> in your browser. Try "run.py -h" to see options.</li>
						<li>Start your work - learn words at <a href="http://127.0.0.1/words">http://127.0.0.1/words</a>
							or listen to a story at <a href="http://127.0.0.1/story">http://127.0.0.1/story</a>.</li>
					</ul>
				</p>

				<h5>Attention!</h5>
				<p>
					<ul>
						<li>The application has its limitations:
							<ul>
								<li>if a language is not supported by a browser,
									then the default language is applied and the word will be pronounced wrong (letter by letter);
								</li>
								<li>the database of words was created in a semi-automated way,
									therefore you can find incorrect words categorization and even translation.
								</li>
							</ul>
						</li>
						<li>The app definitely has lots of bugs because I was focused in exploring dev tools and not in testing to make the app perfect.</li>
						<li>Hence, repeat words after the Parrot, but be careful - parrots are not that smart!
							<br>I take no responsibility if you learn foreign words incorrectly and finally speak some nonexisting language.
						</li>
						<li>In the case of Emergency, please stay calm, go to github and open an issue, or contact me at LinkedIn:
							<a href="https://www.linkedin.com/in/natallia-savelyeva-15407a12a/">https://www.linkedin.com/in/natallia-savelyeva-15407a12a/</a>.
						</li>
					</ul>
				</p>

				<h5>Features:</h5>
				<p>
					<ul>
						<li>Authentication.</li>
						<li>Features for all users:
							<ul>
								<li>search for a word in the database;</li>
								<li>collect words from categories and read them in several languages with optional repeats;</li>
								<li>exclude words from being read;</li>
								<li>load voices available for the required language;</li>
								<li>read a full-text story using the desired language;</li>
								<li>change SpeechSynthesis parameters: voice, volume, rate, pitch;</li>
								<li>statistics: number of unique words, categories and subcategories;</li>
								<li>support options to launch DJ Parrot from command line.</li>
							</ul>
						</li>
						<li>Admin features:
							<ul>
								<li>init/backup/restore the database;</li>
								<li>add a new word into the database;</li>
								<li>translate a word into several languages and read the results aloud.</li>
							</ul>
						</li>
					</ul>
				</p>

				<h5>Why?</h5>
				<p>
					<ul>
						<li>I had the aim of deepening my knowledge and improving my practical skills.</li>
						<li>I desired to study Dutch language and have someone/something reading the words for me.</li>
						<li>I wanted to compare three popular Python-based web frameworks - Flask, Bottle and Django.</li>
						<li>I got inspired by simplicity of Bottle framework and availabilty of speech synthesis in browsers.</li>
					</ul>
				</p>

				<h5>How?</h5>
				<p>
					<ul>
						<li>Back-end: Bottle microframework + Bottle Cork plugin + argparse.</li>
						<li>Database: SQLite 3 (which is inbuilt in Python).</li>
						<li>Frontend: Bootstrap 4 + Font Awesome + JavaScript & jQuery + SpeechSynthesis API.</li>
					</ul>
				</p>

				<hr>
				<p id="statistics"></p>
			</div>
		</div>
		<div class="col">
			% include('_buttons.tpl')				
			% include('_controls.tpl')
			% include('_voices.tpl')
		</div>
	</div>
</div>

% include('_footer.tpl')
