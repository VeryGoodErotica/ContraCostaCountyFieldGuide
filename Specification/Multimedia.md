Multimedia Specification
========================

These specifications are subject to change.

One of the goals behind this field guide is to provide a high quality resource
for those currently living in poverty who can not afford to purchase the print
field guides needed to properly embrace and enjoy the beautiful biological
diversity that exists here in Contra Costa County.

To meet that goal, multimedia content needs to both be of a high quality and
use a license that allows royalty free redistribution in unlimited quantities.

Hopefully those of sufficient financial means will thank the content creators
generous enough to provide high quality content under such a license, so the
attribution of the content creator is important even when the license does not
require such attribution.

These specifications are to help ensure the guidelines are met.


Content Licenses
----------------

Multimedia content __MUST__ have an approved license or it can not be used.

Approved licenses include:

* [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/)
* [CC BY](https://creativecommons.org/licenses/by/4.0/)
* [CC BY SA](https://creativecommons.org/licenses/by-sa/4.0/)
* [Pixabay](https://pixabay.com/service/license/)
* [Verifiable Public Domain](https://copyright.cornell.edu/publicdomain)

For the CC0 and Pixabay licenses, this project *requires* attribution even
though the terms of those licenses do not.

For Public Domain resources, should any be used, attribution is only required
if the content creator is known. Public Domain works *must* be verifiable as
being in the Public Domain according to the requirements listed at the above
*Copyright Information Center* web page provided by the Cornell University
Library.

If you are a multimedia content creator creating content specifically for this
project, the recommended license is [CC BY SA](https://creativecommons.org/licenses/by-sa/4.0/)
but of course you should feel free to use one of the other licenses if that is
your choice. Note that Public Domain is not actually a license, you would have
to have a time machine to create content that is Public Domain, Use CC0 for the
most Public Domain like license if that is your goal and you do not have a time
machine at your disposal.


Wildlife Subjects
-----------------

With many species there can be subtle or even significant phenotype differences
between one region and another. For photographs and video, it is therefore
highly preferable to use actual wildlife from within Contra Costa County.

Using subjects from outside the county is okay if suitable photographs of wild
specimens within the county are not available at the time when writing a page
that benefits from a photograph or video.

In addition to natural selection playing a role in phenotype expression, some
animals have culture— learned behaviors rather than instinctual behaviors. This
may include auditory behavior.

When recording an audio or a video of a behavior, it is therefore preferable to
use actual wildlife within Contra Costa County.

### iNaturalist Record

Especially for wildlife sources within Contra Costa County, a wildlife subject
of a media source if at all possible should have a documented record within the
[iNaturalist](https://www.inaturalist.org/) Citizen Science database.

With a record within that database, proper identification of the speciment is
subject to peer review allowing mistaken identifications to be detected and
corrected.


Vector Illustrations
--------------------

All vector illustrations will use SVG (Scalable Vector Graphics) without
embedded bitmap content.

All vector illustrations MUST comply with WCAG 2.1 AA standards.

Due to rendering issues, text content on an SVG illustration should be done
with an SVG node embedded in the book content page.

The Intel ClearSans font should be used for sans-serif content.
Appropriate fonts for Serif and Monospace content has not yet been decided.

I am generally opposed to the use of Serif fonts, they increase the odds of
triggering reading issues such as with (but no exclusive to) dyslexia.


Bitmap Still Images
-------------------

Until such time that WebP is an ePub core media type (if that ever happens),
photographic content will use JPEG (Joint Photographic Experts Group) and
non-photographic bitmap content will PNG (Portable Network Graphics).

Generally speaking, bitmap images MUST have a minimum resolution of 1024 pixels
on the shortest side.

JPEG images with a resolution below 1536 pixels on the shortest side should use
a 90% quality lossy compression. JPEG images with a resolution of 1536 or
greater on the shorted side should use a 85% quality lossy compression.

If and when WebP becomes an ePub core media type *and* has sufficient support
in portable ePub viewers available to the financially poor, to save space the
standard will change to WebP for both photographic and non-photographic bitmap
images.

The unmodified highest quality version of a bitmap image used should be
archived within the `OriginalResources` directory. Please note that very large
files, such as the raw format many Digital SLR cameras use, are not practical to
track with `git` and should not be committed to the `git` repository. The XML
file describing the original resource however should be committed.


Bitmap Silent Animations
------------------------

Generally speaking, silent animations should be avoided. When they can not be
avoided, GIF (Graphics Interchange Format) should be used *unless* the GIF
limitation of a 256 color pallete is not enough, in which case the animation
should be considered a video.

The unmodified highest quality version of a bitmap silent animation used should
be archived within the `OriginalResources` directory. Please note that very
large files, such as the raw format many Digital SLR cameras use, are not
practical to track with `git` and should not be committed to the `git`
repository. The XML file describing the original resource however should be
committed.


Audio Files
-----------

Until such time that Ogg Opus is supported on iOS/IPadOS devices (if that ever
happens) all audio content will use the AAC (Advanced Audio Coding) HEv1 (High
Efficiency version 1) profile with 96kbps VBR (Variable Bit Rate) *unless* it
can be shown that a higher bitrate is needed to avoid audible compression
artifacts.

Not less than 731 days (two years) after iOS/iPadOS are updated to properly
support the Opus codec in an Ogg container, to save space, this standard will
change to use Ogg Opus encoded at 64kbps *unless* it can be shown that a higher
bitrate is needed to avoid audible compression artifacts.

Audio files should be two-channel stereo, even if both channels contain the
identical content. With lossy compression codecs, using stereo for mono
recording does not significantly increase the file size.

Before lossy encoding, the audio file __MUST__ be volume normalized using the
EBU R128 standard with a target level of `-23 LUFS LU`. After the EBU R128
volume normalization but before the lossy encoding, the audio should be
resampled to a 48kHz sample rate using 24 bits per channel. 48/24 audio is the
standard used for most video productions. While 44.1/16 is good enough for the
human ear, the additional sample rate and bits per sample very little if any
impact on the lossy compressed version of the audio file. The resampling
should use shaped dithering.

When editing an audio file, it is highly recommend you have your audio editing
software use a 48kHz or higher sample rate with 32-bit float bits per sample as
this greatly reduces introduced quantization noise. When you are finished
editing the audio, you can export it to 48kHz/24-bit audio.

When recording an audio file, do __NOT__ record to a lossy codec (especially
not MP3). Recording to AAC HEv1 at a bitrate of 192kbps or higher, or to Ogg
Opus at a bitrate of 128kbps or higher is acceptable if you have insufficient
storage on your recording device for PCM (Pulse Code Modulation) data.

The unmodified highest quality version of the audio recording should be
archived within the `OriginalResources` directory, preferably compressed using
either FLAC (Free Lossless Audio Codec) or ALAC (Apple Lossless Audio Codec).
Please note that very large files, including even short PCM data compressed
with a lossless codec, are not practical to track with `git` and should not be
committed to the `git` repository. The XML file describing the original audio
resource however should be committed.

The modified audio after audio editing but *before* application of EBU R128
loudness normalization should also be archived within the `OriginalResources`
directory, preferably compressed with either FLAC or ALAC. A shell script that
can produce a suitable AAC and Ogg Opus file from the edited version will be
written. Same file size contraints apply. The metadata for the edited audio
should reference the unedited source.


Video Files
-----------

To be written (720p blah blah)


The `OriginalResources` Directory
---------------------------------

The purpose the `OriginalResources` directory is to allow future media editors
to have access to the original source if they feel an alteration would improve
the quality of the resource as used in the ePub book.

For example, a media editor who is very skilled with Adobe Photoshop may know
how to make an image look better than I do. With access to the original `.CR2`
file from my camera, they may be able to do a much better job than if they had
to start with the cropped and resolution reduced `.jpg` file.

A secondary purpose is to allow for better lossy compression (e.g. WebP for
images and Ogg Opus for audio) as it becomes available to reduce the size of
the distributed ePub.

Many original source files are way too large to host within a git repository.
A solution for hosting them has not yet been looked for, preferably a host with
both the ability to fetch an individual file as needed or to use `rsync` or
a related tool to grab them all.

For the purpose of avoiding name collisions and for allowing validating the
integrity of an original source file, they are named with a UUID created by
first taking the SHA-356 hash of the file, and then a MD5SUM of that hash.

Even though it is paranoia, the double hash is used to avoid the vulnerabilities
of MD5SUM to intentional collisions. If and when a collision vulnerability is
found in SHA-356 that algorithm can be swapped for another with a renaming of
all the existing resources to match.

The python script `resource-UUID.py` in the `tools/` directory will create a
UUID from an original source file and copy the source file to the new name.
You should do a checksum of both the originally named file and the copied file
with a new name just to make sure there has not been an error in copying. I
will build that into the script in the future.

### Metadata XML File

Each Original Resource __MUST__ have an accompanying XML file with information
about the original file. The specification for this file is still being thought
out.

The root node of this XML file is the `<Resource type="">` node. The `type`
attribute can have a value of:

* `photograph`
* `illustration`
* `animation`
* `audio`
* `video`

The first child node will be an `<original>` node which points to the name of
the file the file being described was created from. In the event the file was
not created from another file, then it will be the file name of the file being
described.

For example, the file `dec9b5f4-b140-4d90-8c64-ed887fc47813.CR2` was created
by the act of snapping a shutter on a DSLR. Since there is not an upstream file
it was created from, the `dec9b5f4-b140-4d90-8c64-ed887fc47813.xml` file would
have `dec9b5f4-b140-4d90-8c64-ed887fc47813.CR2` as the text child of the
`<original>` node.

However if Adobe Photoshop was used to clean up the photo, the photoshop user
may want to archive the photoshop `.psd` file. That file would have a different
filename, but would also have `dec9b5f4-b140-4d90-8c64-ed887fc47813.CR2` as the
text child of the `<original>` node.

In cases like a Photoshop file (or in the final result used withing the ePub)
a `<checksum algo="">` node __MUST__ exist directly after the `<original>`
node. Like the `<original>` node, it contains a single text string, but the
string is not a UUID. Rather, it is a checksum of the file, using the algorithm
described in the `algo` attribute. At this time the following algorithms are
allowed:

* `sha256`
* `sha384`

More may be added in the future.
