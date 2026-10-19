# Nebula Bulldog

**A refined, modern digital audio workstation with the soul of a vintage console.**

Nebula Bulldog is a full-featured digital audio workstation for recording, editing,
mixing and mastering audio and MIDI. It is built for audio engineers, musicians,
soundtrack editors and composers who want a professional mixing environment that
looks and feels like a classic analog console.

## Oldschool console look

The centerpiece of Nebula Bulldog is its mixer. Every channel strip, fader, knob,
meter and button has been reimagined with an oldschool console aesthetic:

- **Dark rack chassis** — deep charcoal and brushed-metal paneling that evokes a
  vintage outboard rack.
- **Amber VU meters** — warm, glowing meter bridges that react to your signal like
  the real thing.
- **Chrome-finished knobs** — tactile, rotary controls with the look of classic
  console hardware.
- **Vintage-style buttons** — record, solo and mute buttons styled like the illuminated
  switches found on legendary mixing desks.

The result is a DAW that feels like hardware: immediate, tactile, and full of
character — without any of the clutter of a modern computer interface.

## Built on Ardour

Nebula Bulldog is a refined take on Ardour, the powerful open-source digital audio
workstation. It keeps Ardour's robust recording, editing, mixing and routing engine
and wraps it in a completely re-styled, console-inspired user interface.

Key capabilities include:

- Multitrack audio and MIDI recording
- Non-destructive editing with flexible playlists and regions
- Full-featured mixer with sends, inserts, VCA groups and automation
- LV2, LADSPA and plugin support
- Jack / ALSA / CoreAudio / PulseAudio audio backends
- Extensive control-surface and MIDI mapping support

## What's different

| Ardour | Nebula Bulldog |
|--------|--------------|
| Modern flat interface | Oldschool analog-console interface |
| Standard meters | Amber VU-meter bridge |
| Plain faders | Console-style faders on a dark chassis |
| Generic buttons | Vintage illuminated console switches |

No manufacturer logos or third-party trademarks are used anywhere in Nebula
Bulldog. The GUI is described as having an "oldschool console look" and is an
original visual reinterpretation.

## Getting started

Nebula Bulldog is built with the Ardour build system (waf). See the Ardour
documentation for build dependencies and instructions, then configure with:

```
./waf configure
./waf
```

To build with a custom name:

```
./waf configure --program-name="Nebula Bulldog"
```

## License

Nebula Bulldog is free software released under the GNU General Public License
version 2 or later. See the `COPYING` file for details.

---

**Nebula Bulldog** — where modern DAW power meets classic console character.
