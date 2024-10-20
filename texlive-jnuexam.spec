Name:		texlive-jnuexam
Version:	71883
Release:	1
Summary:	Exam class for Jinan University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jnuexam
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jnuexam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jnuexam.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an exam class for Jinan University
(China).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jnuexam
%doc %{_texmfdistdir}/doc/latex/jnuexam

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
