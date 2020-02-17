Resource Metadata File
======================

Resource Metadata Files should be maintained by a species group curator. The
authors of content are not responsible for maintaing these files, only a group
curator can add non-text resources to the project.

Each non-text resource within the `OriginalResource` directory or within the
`OEBPS` directory __MUST__ have an accompanying XML file describing the
resource, including the license terms for use of the resource.

The XML used is of my own invention and is not an official standard. It is
subject to change as needed.

The XML file shall have the same file name as non-text resource it describes,
but with a `.xml` file extension rather than the file extension of the non-text
resource that it describes.

When within the `OEBPS` directory, an entry for the Resource Metadata File
__MUST__ be made withing the `<manifest>` node of the `content.opf` file and
use the `media-type="text/xml"` attribute. For non-text files within the
`OriginalResource` directory, no entries in the `content.opf` file are needed.

The Root `<Resource type="" xml:lang="en-US">` Node
---------------------------------------------------

This is the XML `root` node for the file. The `type` attribute is __REQUIRED__
and should be a value from the following list:

* `photograph`
* `illustration`
* `animation`
* `audio`
* `video`
* `font`

If additional types are needed, they can be added.

The `xml:lang` attribute __MUST__ be present and set to `en-US`.

If this Contra Costa County project takes off and someone in France or Brazil
or Kenya or wherever wants to use this project as a model, then they can use
whatever floats their boat, but for this ePub the Resource Meta Files are to be
authored in American English.

Translations of the project to Spanish will be wanted, Contra Costa County has
enough of a Spanish speaking community that I believe it is necessary, but the
resource metadata files need to be in American English.

### The `<original>` Node

This node is required and must have a single text string child, the name of the
file within the `OriginalResources` directory used as a source to create the
file being described.

If the resource file being described was not created from another file, then
the contents of node will be the file name for the file being described.

For example, the file `60392b63-35b7-42aa-8103-ecc31a4ccd5e.CR2` was created by
snapping the shutter on a camera. There is no upstream file, so the matching
Resource Metadata file `60392b63-35b7-42aa-8103-ecc31a4ccd5e.xml` would have
`60392b63-35b7-42aa-8103-ecc31a4ccd5e.CR2` as the text string within the
`<original>` node.

If Adobe Photoshop was used to manipulate the image, there would be a Photoshop
`.psd` file that could be named something like `27c9b1ee-3d37-40e0-873b-4142b02bc225.psd`.
That photoshop file would be accompanied by a `27c9b1ee-3d37-40e0-873b-4142b02bc225.xml`
file but since it was created from the `.CR2` file, the `<original>` node would
contain `60392b63-35b7-42aa-8103-ecc31a4ccd5e.CR2`.

However if the file `Cover-White-crowned_Sparrow.jpg` within the `OEBPD`
directory was creating by cropping the photoshop file, then the accompanying
`Cover-White-crowned_Sparrow.xml` file would list `27c9b1ee-3d37-40e0-873b-4142b02bc225.psd`
as the string child of the `<original>` node.

### The `<checksum algo="">` Node

Resources within the `OriginalResources` directory have a checksum built-in to
the filename. The integrity of those files is easy to validate. However
resources within the `OEBPS` directory use a more human friendly filename.

To facilitate verification that the metadata within the XML file applies to the
file with a name match, the `<checksum algo="">` node __MUST__ be used.

For example, the `Cover-White-crowned_Sparrow.xml` file would be __REQUIRED__
to have a `<checksum algo="">` node containing a hash checksum of the
`Cover-White-crowned_Sparrow.jpg` file. This facilitates automated validation
before publishing that the metadata files match the resource.

For the `algo=""` attribute, presently only the following two options are
available:

* `sha256`
* `sha384`

Generally speaking `sha256` is what should be used. If and when a collision in
`sha256` is found, the project can switch to `sha384` while investigating other
hashing algorithms.

### The `<flaws>` Node

This is node without parameters that contains a single text string as a child.
This node should be direct child of the `<Resource/>` node. There may be more
that one `<flaws>` node, though it is okay for multiple flaws to be detailed
within a single node.

There will many instances where a resource has a known flaw but is better than
nothing. For example, an image may be over-exposed or need some photoshop work
or the subject may be from a specimen photographed outside the county.

In such cases, the *optional* `<flaws>` node can be used to keep track of the
flaws so that it is easier to identify what work needs to be done or what
resources potentially need alternatives found.

### The `<creator type="">` Node

This node specifies a creator of the resource. There may be more than but there
must be *at least* one.

The type attribute must be one of the following:

* photographer
* videographer
* illustrator
* recordist
* typedesigner

Other values may be added if needed.