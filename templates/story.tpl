% include('_header.tpl', title='DJ Parrot - Read')
<div class="container">
	<div class="row">
		<div class="col-9">
			% include('_nav_bar.tpl')
			<select id="stories" class="form-control" name="stories">
				% for story, description in sorted(stories.items()):
				<option value="{{ story }}"
					% if "grammar" in story:
						selected 
					% end
				>
					{{ description }}
				</option>
				% end
			</select>
			<textarea id="longtext" class="form-control" rows="20" placeholder="Please enter the text">
arise, arose, arisen.
awake, awoke, awoken.
be, was/were, been.
bear, bore, born(e).
beat, beat, beaten.
become, became, become.
begin, began, begun.
bend, bent, bent.
bet, bet, bet.
bind, bound, bound.
bite, bit, bitten.
bleed, bled, bled.
blow, blew, blown.
break, broke, broken.
breed, bred, bred.
bring, brought, brought.
broadcast, broadcast, broadcast.
build, built, built.
burn, burnt or burned, burnt or burned.
burst, burst, burst.
buy, bought, bought.
can, could, been able.
catch, caught, caught.
choose, chose, chosen.
cling, clung, clung.
come, came, come.
cost, cost, cost.
creep, crept, crept.
cut, cut, cut.
deal, dealt, dealt.
dig, dug, dug.
do, did, done.
draw, drew, drawn.
dream, dreamt or dreamed, dreamt or dreamed.
drink, drank, drunk.
drive, drove, driven.
eat, ate, eaten.
fall, fell, fallen.
feed, fed, fed.
feel, felt, felt.
fight, fought, fought.
find, found, found.
fly, flew, flown.
forbid, forbade, forbidden.
forget, forgot, forgotten.
forgive, forgave, forgiven.
freeze, froze, frozen.
get, got, got.
give, gave, given.
go, went, gone.
grind, ground, ground.
grow, grew, grown.
hang, hung, hung.
have, had, had.
hear, heard, heard.
hide, hid, hidden.
hit, hit, hit.
hold, held, held.
hurt, hurt, hurt.
keep, kept, kept.
kneel, knelt, knelt.
know, knew, known.
lay, laid, laid.
lead, led, led.
lean, leant or leaned, leant or leaned.
learn, learnt or learned, learnt or learned.
leave, left, left.
lent, lent, lent.
lie (in bed), lay, lain.
lie (to not tell the truth), lied, lied.
light, lit or lighted, lit or lighted.
lose, lost, lost.
make, made, made.
may, might, ….
mean, meant, meant.
meet, met, met.
mow, mowed, mown or mowed.
must, had to, ….
overtake, overtook, overtaken.
pay, paid, paid.
put, put, put.
read, read, read.
ride, rode, ridden.
ring, rang, rung.
rise, rose, risen.
run, ran, run.
saw, sawed, sawn or sawed.
say, said, said.
see, saw, seen.
sell, sold, sold.
send, sent, sent.
set, set, set.
sew, sewed, sewn or sewed.
shake, shook, shaken.
shall, should, ….
shed, shed, shed.
shine, shone, shone.
shoot, shot, shot.
show, showed, shown.
shrink, shrank, shrunk.
shut, shut, shut.
sing, sang, sung.
sink, sank, sunk.
sit, sat, sat.
sleep, slept, slept.
slide, slid, slid.
smell, smelt, smelt.
sow, sowed, sown or sowed.
speak, spoke, spoken.
spell, spelt or spelled, spelt or spelled.
spend, spent, spent
spill, spilt or spilled, spilt or spilled.
spit, spat, spat.
spread, spread, spread.
stand, stood, stood.
steal, stole, stolen.
stick, stuck, stuck.
sting, stung, stung.
stink, stank, stunk.
strike, struck, struck.
swear, swore, sworn.
sweep, swept, swept.
swell, swelled, swollen or swelled
swim, swam, swum.
swing, swung, swung.
take, took, taken.
teach, taught, taught.
tear, tore, torn.
tell, told, told.
think, thought, thought.
throw, threw, thrown.
understand, understood, understood.
wake, woke, woken.
wear, wore, worn.
weep, wept, wept.
will, would, ….
win, won, won.
wind, wound, wound.
write, wrote, written.
			</textarea>

			<hr>
			<p id="statistics"></p>

		</div>
		<div class="col">
			% include('_buttons.tpl')
			% include('_controls.tpl')
			% include('_v_languages.tpl')
			% include('_voices.tpl')
		</div>
	</div>
</div>

% include('_footer.tpl')
