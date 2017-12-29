# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/algorithmicx
# catalog-date 2006-10-12 12:11:58 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-algorithmicx
Version:	20170414
Release:	1
Summary:	The algorithmic style you always wanted
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/algorithmicx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Algorithmicx provides a very flexible, yet easy to use way for
inserting good looking pseudocode or source code in your
papers. It has built in support for Pseudocode, Pascal, C, and
powerful means to create definitions for any programming
language. You can easily adapt a Pseudocode style to your
native language.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061012-2
+ Revision: 749160
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061012-1
+ Revision: 717812
- texlive-algorithmicx
- texlive-algorithmicx
- texlive-algorithmicx
- texlive-algorithmicx
- texlive-algorithmicx

