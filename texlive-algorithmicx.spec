%global tl_name algorithmicx
%global tl_revision 78101

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The algorithmic style you always wanted
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algorithmicx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Algorithmicx provides a flexible, yet easy to use, way for inserting
good looking pseudocode or source code in your papers. It has built in
support for Pseudocode, Pascal and C, and offers powerful means to
create definitions for any programming language. The user can adapt a
Pseudocode style to his native language.

