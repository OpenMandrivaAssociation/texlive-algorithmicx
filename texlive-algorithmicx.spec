Name:		texlive-algorithmicx
Version:	20061012
Release:	1
Summary:	The algorithmic style you always wanted
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/algorithmicx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Algorithmicx provides a very flexible, yet easy to use way for
inserting good looking pseudocode or source code in your
papers. It has built in support for Pseudocode, Pascal, C, and
powerful means to create definitions for any programming
language. You can easily adapt a Pseudocode style to your
native language.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/algorithmicx/algc.sty
%{_texmfdistdir}/tex/latex/algorithmicx/algcompatible.sty
%{_texmfdistdir}/tex/latex/algorithmicx/algmatlab.sty
%{_texmfdistdir}/tex/latex/algorithmicx/algorithmicx.sty
%{_texmfdistdir}/tex/latex/algorithmicx/algpascal.sty
%{_texmfdistdir}/tex/latex/algorithmicx/algpseudocode.sty
%doc %{_texmfdistdir}/doc/latex/algorithmicx/README
%doc %{_texmfdistdir}/doc/latex/algorithmicx/algorithmicx.pdf
%doc %{_texmfdistdir}/doc/latex/algorithmicx/algorithmicx.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
