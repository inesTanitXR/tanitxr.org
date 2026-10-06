# Embassy event, 22 October 2026, 6pm to 8pm

Planning note written 2026-10-06. Sixteen days out.

## The dates that actually bind

| | |
|---|---|
| **Fri 9 Oct** | Newsletter edition 20 goes out. The only edition before the event. The event has to be in it. |
| **Fri 16 Oct** | Sign-ups close, end of day |
| **Sat 17 Oct** | Ines compiles the list and checks it |
| **Sun 18 Oct** | Guest list to the embassy, four days ahead as they asked |
| **Thu 22 Oct** | Event, 6pm to 8pm |

Closing on the 16th rather than the 18th leaves a day of slack. A list sent late to an embassy
is not a list.

## Sign-up: use a Google Form, not our own form

This is the one case where I would not build it ourselves, for a reason that is not about
Google being nicer.

**Our form path is not reliable enough for this.** Site forms post to FormSubmit, which on
30 September returned Cloudflare 522s and sixty second timeouts for hours. A lost newsletter
signup is a shame. A lost guest list entry is somebody turned away at an embassy door.

**The data is more sensitive than usual.** Embassies normally want full legal name as it
appears on ID, and often nationality and an ID or passport number. Routing that through a free
third-party relay that forwards it as email is not good practice. A Google Form writes
straight into a Sheet that Ines owns.

**And she has to hand the embassy a list.** A Sheet exports. An inbox does not.

**Ask the embassy first:** do they need ID or passport numbers, or only names? It changes the
form and it changes the next decision.

- **Names only** → embed the form in the Tanit page. People stay on our site, conversion is higher.
- **ID numbers** → link out to the Google Form with a large button instead. Seeing `google.com`
  in the address bar is worth more than keeping them on our page when they are typing a
  passport number.

Either way the page carries everything else and the form is only the last step.

### Fields to put in the form

Required
- Full name, exactly as on the ID you will bring
- Email
- Country or city you are coming from
- Organisation or role, optional but the embassy likes it

Only if the embassy asks for them
- Nationality
- ID or passport number
- Date of birth

Useful to us, not to them
- How did you hear about this
- Anything we should know (access needs, dietary)
- Tick box: happy to be added to the Tanit XR newsletter

Add a line at the top of the form saying the list goes to the embassy for security clearance
and nothing else, and that sign-ups close on 16 October.

**Google Forms cannot close itself on a date.** Either Ines switches "accepting responses" off
on the 16th, or we add a small Apps Script trigger. She already has an Apps Script deployment,
so the trigger is half an hour of work if she wants it automatic.

## Promotion, for the international attendance the embassy asked for

### Do these

1. **A LinkedIn Event.** Free, and LinkedIn is Ines's strongest channel by a distance. Her
   following is exactly the international XR and heritage audience the embassy wants. People
   can mark attending, and LinkedIn then reminds them. This is the highest-yield single action.
2. **Newsletter edition 20, Friday 9 October.** Already scheduled, already written to that
   audience, and the last one before the event. Put it at the top, not in the listings.
3. **Ask the embassy to promote it.** They asked for international attendance, so it is their
   interest too, and they have a diplomatic mailing list and cultural network that reaches
   people we cannot. Costs nothing and is the easiest thing on this list to forget.
4. **Instagram and Facebook**, with the carousel generator we already have.
5. **XR community channels**: XR Women, the AWE community, the XR Guild, relevant Discords.
   Free, and international by nature.

### On Meetup

I would skip it. Meetup charges the organiser a subscription, which is the opposite direction
to the cancellations in progress, and Meetup is built around local city groups, which is the
opposite of international reach. Its penetration in Tunis is thin.

If something like it is wanted, **Eventbrite** is free for free events, has real international
discovery, and exports an attendee list. It could even replace the Google Form, though it is
weaker for ID-number fields.

## The page

The site already has an events system (`EVENTS` in build.py, cards with date, place and links,
and dedicated pages like `immersegt-2026.html`), so this slots into the existing pattern rather
than needing anything new.

### What I need from Ines before building it

- Which embassy, and the exact wording they want for their own name
- The event title and two or three sentences on what it is
- The full address, and which entrance
- Dress code, and what people must bring to get in
- Whether there is a guest cap
- Whether photography is allowed
- The Google Form link, once it exists

Everything else I can write.
