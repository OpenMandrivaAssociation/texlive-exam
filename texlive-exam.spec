# revision 22585
# category Package
# catalog-ctan /macros/latex/contrib/exam
# catalog-date 2011-05-23 10:42:55 +0200
# catalog-license lppl1.3
# catalog-version 2.4
Name:		texlive-exam
Version:	2.4
Release:	8
Summary:	Package for typesetting exam scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exam
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a class exam, which eases production of exams, even by
a LaTeX novice. Simple commands are provided to: - create
questions, parts of questions, subparts of parts, and
subsubparts of subparts, all with optional point values; -
create a grading table, indexed either by question number
(listing each question and the total possible points for that
question) or by page number (listing each page with points and
the total possible points for that page); - create headers and
footers that are each specified in three parts: one part to be
left justified, one part to be centered, and one part to be
right justified, in the manner of fancyhdr Headers and/or
footers can be different on the first page of the exam, can be
different on the last page of the exam, and can vary depending
on whether the page number is odd or even, or on whether the
current page continues a question from a previous page, or on
whether the last question on the current page continues onto
the following page. Multiple line headers and/or footers are
allowed, and it's easy to increase the part of the page devoted
to headers and/or footers to allow for this. Note that the
bundle exams also provides a file exam.cls; the two bundles
therefore clash, and should not be installed on the same
system.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/exam/exam.cls
%doc %{_texmfdistdir}/doc/latex/exam/README
%doc %{_texmfdistdir}/doc/latex/exam/exam-2.4.md5
%doc %{_texmfdistdir}/doc/latex/exam/examdoc.pdf
%doc %{_texmfdistdir}/doc/latex/exam/examdoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4-2
+ Revision: 751671
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4-1
+ Revision: 718394
- texlive-exam
- texlive-exam
- texlive-exam
- texlive-exam

