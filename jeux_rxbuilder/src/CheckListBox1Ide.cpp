//---------------------------------------------------------------------------

#include <vcl.h>

#pragma hdrstop

#include "CheckListBox1.h"
#pragma package(smart_init)
//---------------------------------------------------------------------------
// ValidCtrCheck est utilis�e pour garantir que les composants cr��s n'ont pas
// de fonctions virtuelles pures.
//

static inline void ValidCtrCheck(TCheckListBoxTst *)
{
	new TCheckListBoxTst(NULL);
}
//---------------------------------------------------------------------------

//---------------------------------------------------------------------------
namespace Checklistbox1
{
	void __fastcall PACKAGE Register()
	{
		TComponentClass classes[1] = {__classid(TCheckListBoxTst)};
		RegisterComponents(L"Tst", classes, 0);
	}
}
//---------------------------------------------------------------------------
