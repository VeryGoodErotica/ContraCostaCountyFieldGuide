Field Guide Specification
=========================

If this dream becomes reality, this project will grow in size and become huge.

Specifications must be created so that multiple people can collaborate and work
together on this project.

At least initially, I propose the following hierarchical structure:


Chief Editor
------------

The chief editor is responsible for the project as a whole, for reviewing pull
requests from taxon curators and rejecting or accepting them as needed, for
making sure the ePub that is distributed is of the highest quality possible.


Taxon Curator
-------------

An editor responsible for a particular taxonomy group. For example, it is
likely that all Reptiles and Amphibians would be considered tohether as a
taxon group with a single curator responsible for the content related to
that group.

On the other hand, Insects is probably such a large grouping that it would
require multiple groupings with multiple taxon curators in order to keep
the quality high.

A Taxon Curator should be passionate and well-informed about the taxon
group they are responsible for, but also must be technical savvy.

To that end, team curation with two (or more) people working together may
be used.


Content Author
--------------

A naturalist who wished to write species descriptions, identification keys,
and other written content within the ePub spine. A Taxon Curator likely will
double as a Content Author but that does not need to be the case.

A Content Author will clone the `git` repository relevant to the taxon group
they are creating content for. After creating their content, the Content Author
will submit a pull request to the Taxon Curator. The Taxon Curator, when they
are satisfied with the added content within their taxon group, will then do a
pull request with the main development branch.


Branch Issues
-------------

Merging different branches in `git` can sometimes be tricky if multiple people
are working on the same file.

For this reason, it is my position that only a Taxon Curator should be able to
add files to their branch. They can add a stuff for the file to be created by
a Content Author and the Content Author then only edits the files they have
been given permission to work on.

When things like grammar are being worked on by someone other than the Content
Author responsible for the content, the Content Author should probably refrain
from editing their branch until the Taxon Curator has accepted the pull request
of the other editors so that the Content Author can sync their branch etc.

Some of these git management protocols will have to be figured out as time
goes on. Hopefully merge issues are rare.

But I got this.
