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